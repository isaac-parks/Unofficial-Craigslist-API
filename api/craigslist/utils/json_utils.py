import json

def parse_json(data):
    body_unicode = data.decode('utf-8')
    body = json.loads(body_unicode)
    return body['data']