import json
from bson import ObjectId


def objectIdToId(data):
    data['id'] = str(data['_id'])
    del (data['_id'])
    return data


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
