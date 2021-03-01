import redis
import pandas as pd


def cache_df(data):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.setex('df', 60, data.to_json())


def get_df():
    r = redis.Redis(host='localhost', port=6379, db=0)
    df = r.get('df')
    return pd.read_json(df)
