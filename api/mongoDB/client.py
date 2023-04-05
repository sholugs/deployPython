import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

try:
    db = MongoClient("mongodb+srv://sanvaproject:G1TpffE8mFgnT7rs@sanvaproject.admqgp1.mongodb.net/?retryWrites=true&w=majority")
    db_name = "test" 
    db = db[db_name]
    print("Connected to MongoDB")
except ConnectionFailure as e:
    print("Could not connect to MongoDB: %s" % e) 