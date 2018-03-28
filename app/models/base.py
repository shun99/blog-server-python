import time
from bson import ObjectId
from app import mongo


class BaseModel(object):
    def __init__(self, create_time=int(time.time()), update_time=int(time.time())):
        self.update_time = update_time
        self.create_time = create_time
