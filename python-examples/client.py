import pymongo
from config import config

client = pymongo.MongoClient(config['uri'], username=config['username'], password=config['password'])
database = client["database"]
collection = database["collection"]