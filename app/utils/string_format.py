import json
from bson import ObjectId


def objectIdToId(data):
    data['id'] = str(data['_id'])
    del (data['_id'])
    return data


def data_to_api(data, **kwargs):
    response = {
        "code": kwargs.get('code', 0),
        "data": data,
        "haveMore": kwargs.get('haveMore', False)
    }
    return response


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
