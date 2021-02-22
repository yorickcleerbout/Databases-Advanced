import time
from scraper import scrape
from mongoDB import create_connection_to_collection


def main():
    col = create_connection_to_collection()
    data = scrape()
    col.insert_one(data)


if __name__ == "__main__":
    while True:
        try:
            main()
        except:
            main()
        time.sleep(60)
