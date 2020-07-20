import MeCab
from bs4 import BeautifulSoup


def main(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        if request.args.get('type')=='0':
            return request.args.get('value')
        elif  request.args.get('type')=='1':
            return request.args.get('value')
        else :
            return 'invalid type'

