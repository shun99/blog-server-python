import time
from app import mongo
from utils import JSONEncoder
from bson import ObjectId


class BaseModel(object):
    def __init__(self, create_time=time.time(), update_time=time.time()):
        self.update_time = update_time
        self.create_time = create_time
