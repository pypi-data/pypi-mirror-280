from pymongo import MongoClient
from os import getenv

MONGO_URL = getenv('MONGO_URL')
MONGO_DB = getenv('MONGO_DB')


def connect():
    if not MONGO_URL or not MONGO_DB:
        raise Exception('Need to setup MONGO_URL and MONGO_DB environments variables')

    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    return client[MONGO_DB]


class Singleton(type):
    __instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class ConnectMongo(metaclass=Singleton):
    def __init__(self):
        self.mongo_url = MONGO_URL
        self.mongo_db = MONGO_DB
        self.db = connect()


