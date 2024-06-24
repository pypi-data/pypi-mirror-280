from asgiref.sync import sync_to_async
from auditlog.context import set_actor
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from graphql_jwt.shortcuts import get_user_by_token


class JwtAuthMiddleware(BaseMiddleware):
    """
    This middleware for JWT authentication in WebSocket connections.

    Checks the 'authorization' header for a JWT token, retrieves the corresponding user,
    and adds the user to the connection scope.

    If the token is invalid or not provided, sets the user to AnonymousUser.
    Use here : 
    'websocket': JwtAuthMiddleware(
        AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        )
    )
    """
    async def __call__(self, scope, receive, send):
        """
        Process the connection scope to authenticate the user.

        :param scope: The connection scope containing headers and other connection details
        :param receive: Callable to receive messages
        :param send: Callable to send messages
        :return: Calls the next middleware or application
        """
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            auth_header = headers[b'authorization'].decode()
            if auth_header.startswith('JWT '):
                token = auth_header.split('JWT ')[1]
                try:
                    user = await sync_to_async(get_user_by_token)(token)
                    scope['user'] = user
                except Exception as e:
                    scope['user'] = AnonymousUser()
            else:
                scope['user'] = AnonymousUser()
        else:
            scope['user'] = AnonymousUser()
        return await super().__call__(scope, receive, send)
    


class AuditActorMiddleware:
    """
    Integrating `django-auditlog` with this middleware in a Django project involves adding `django-auditlog` 
    to `requirements.txt`, installing it, and including it in `INSTALLED_APPS`. Define `AuditActorMiddleware` 
    to set the actor for auditing based on an authorization token or request user, and add it to the `MIDDLEWARE` 
    list in `settings.py`. Implement supporting functions to retrieve users by token and set the actor globally. 
    Register models for auditing using `auditlog.register`. After setting up, run migrations and start the server 
    to enable auditing functionality, logging changes with actor information.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        header = request.headers.get('Authorization')
        if header:
            try:
                token = header.split()[1].strip()
                user = get_user_by_token(token=token)
            except:
                user = None
        else:
            user = request.user

        set_actor.actor = user
        response = self.get_response(request)
        return response
