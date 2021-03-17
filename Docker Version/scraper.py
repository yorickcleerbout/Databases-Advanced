from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time
import redis


def cache_df(data):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.setex('df', 60, data.to_json())


def scrape():
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    response = get(url)
    HTML = BeautifulSoup(response.text, 'html.parser')
    hashes = HTML.find_all(
        'a', class_='sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK')
    extra = HTML.find_all(
        'span', class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')

    hashes = [h.contents[0] for h in hashes]
    extra = [e.contents[0].replace('$', '').replace(',', '') for e in extra]

    newlist = []
    index = 0
    for iterations in range(150 // 3):
        i = iterations * 3
        newlist.append(
            [hashes[index], extra[i], extra[i+1], float(extra[i+2])])
        index += 1

    df = pd.DataFrame(newlist, columns=[
                      'Hash', 'Time', 'Amount (BTC)', 'Amount (USD)'])

    # SAVE TO REDIS
    cache_df(df)
    # return df


while True:
    try:
        scrape()
    except:
        pass
    time.sleep(60)
