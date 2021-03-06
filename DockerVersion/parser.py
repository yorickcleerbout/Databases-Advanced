import pandas as pd
import redis
import pymongo as mongo
import json
import time


def get_df():
    r = redis.Redis(host='redis', port=6379, db=0)
    df = r.get('df')
    return pd.read_json(df)


def filter_highest():
    df = get_df()
    return df.sort_values(by=['Amount (USD)'], ascending=False).head(1)


def create_connection_to_collection():
    client = mongo.MongoClient("mongodb://mongo:27017")
    transactions_db = client["Databases-Advanced"]
    return transactions_db["BTC-Transactions"]


def save_to_mongo(data):
    json_df = data.to_json(orient='records')
    to_save = json.loads(json_df.replace('[', '').replace(']', ''))
    col = create_connection_to_collection()
    col.insert_one(to_save)


# FILTER HIGHEST TRADE AND SAVE TO MONGO
while True:
    try:
        highestValue = filter_highest()
        print("About to save to MongoDB")
        save_to_mongo(highestValue)
    except:
        pass
    time.sleep(60)
