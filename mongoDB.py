import pymongo as mongo
import json


def create_connection_to_collection():
    client = mongo.MongoClient("mongodb://127.0.0.1:27017")
    transactions_db = client["Databases-Advanced"]
    return transactions_db["BTC-Transactions"]


def save_to_mongo(data):
    json_df = data.to_json(orient='records')
    to_save = json.loads(json_df.replace('[', '').replace(']', ''))
    col = create_connection_to_collection()
    col.insert_one(to_save)
