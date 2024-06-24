import json
from graphql import GraphQLError


def get_response(message_en, message_pt, status_code, success):
    response = {
        'message_en': message_en,
        'message_pt': message_pt,
        'status_code': status_code,
        'success': success,
        }
    return response

def error_response(e):
    response = json.dumps({
        "success": False,
        "error_code" : getattr(e, 'code', 404),
        "message": e.message if hasattr(e, 'message') else str(e) or e.__class__.__name__
    })
    raise GraphQLError(response)
