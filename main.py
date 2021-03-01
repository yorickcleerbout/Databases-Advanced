import time
from scraper import scrape
from mongoDB import save_to_mongo
from redisDB import cache_df
from parser import filter_highest


def main():
    try:
        data = scrape()
    except:
        data = scrape()

    cache_df(data)

    highestValue = filter_highest()
    save_to_mongo(highestValue)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
