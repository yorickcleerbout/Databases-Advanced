import pymongo as mongo
import json


def create_connection_to_collection():
    client = mongo.MongoClient("mongodb://127.0.0.1:27017")
    transactions_db = client["Databases-Advanced"]
    return transactions_db["BTC-Transactions"]
