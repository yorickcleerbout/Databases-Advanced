import pandas as pd
from redisDB import get_df


def filter_highest():
    df = get_df()
    return df.sort_values(by=['Amount (USD)'], ascending=False).head(1)
