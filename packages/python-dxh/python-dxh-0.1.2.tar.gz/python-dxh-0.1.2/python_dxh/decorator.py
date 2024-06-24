from django.db.models import Q
from graphene import Connection, Int
from graphql import GraphQLError


def authenticate_role(allowed_groups):
    '''
    This decorator is used to authenticate a user based on the groups they belong to.
    '''
    def decorator(func):
        def wrap(*args, **kwargs):
            info = args[1]
            user = info.context.user
            q_objects = Q()
            for group in allowed_groups:
                q_objects |= Q(name__iexact=group)
            if user.is_superuser or user.groups.filter(q_objects).exists():
                group_names = list(user.groups.values_list('name', flat=True))
                return func(*args, **kwargs)
            else:
                response_message = {
                    "message_en": "You are not authorized to perform this action.",
                    "message_pt": "Você não está autorizado a realizar esta ação.",
                    "status_code": 404,
                    "success": False,
                }
                raise GraphQLError(response_message)
        return wrap
    return decorator

'''
Use example:
@authenticate_role(['Admin', 'Manager'])
def resolve_create_employee(self, info, **kwargs):
    pass
'''

