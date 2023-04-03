import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

try:
    db = MongoClient(os.getenv("MONGO_URI"))
    db_name = "test" 
    db = db[db_name]
    print("Connected to MongoDB")
except ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e) 