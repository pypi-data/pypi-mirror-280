from datetime import datetime
from urllib.parse import parse_qs, unquote, urlparse

from graphene import Connection, Int


def get_access_key_by_url(url):
    '''
    Extract the 44 digit access key from the URL.
    '''
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    key = query_params.get('p', [None])[0]
    if key:
        key = unquote(key)
        parts = key.split('|')
        if parts and len(parts[0]) == 44:
            return parts[0]
    return None


class ExtendedConnection(Connection):
    '''
    This class is used to extend the Connection class in graphene 
    to add additional fields like total_count and edge_count.
    '''
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length

    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)
