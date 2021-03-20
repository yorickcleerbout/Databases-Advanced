<img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" /><img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/><img alt="Pandas" src="https://img.shields.io/badge/pandas%20-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" /><img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?&style=for-the-badge&logo=mongodb&logoColor=white"/><img alt="Docker" src="https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white"/>

# Databases Advanced

This repository is made as part of a assignment of the course 'Databases Advanced', the intention of this assignment is to get familiar with services like MongoDB, Docker, Virtual Machines etc. To keep this assignment clear and easy to understand we splitted this task in multiple smaller tasks.

## Task 1: Python Webscraper

The first task is to scrape the [Blockcain website](https://www.blockchain.com/btc/unconfirmed-transactions) for all the current [Bitcoin (BTC)](https://nl.wikipedia.org/wiki/Bitcoin) transactions all over the world. The output of this part of the assignment has to be the highest **USD** value at the moment of scraping. When you are running a webscraper permanently it can become quite heavy for your computer thats why I recommend running this in a cloud based environment or virutual machine and running the script once every minute. (For me it is running on an Ubuntu Virtual Machine)

### Usage:

**Step 1: Clone my repository**
<br>
<code>git clone https://github.com/yorickcleerbout/Databases-Advanced.git</code>
<br>
<br>
**Step 2: Install required python packages**
<br>
<code>pip3 install -r requirements.txt</code>
<br>
<br>
**Step 3: Make the python script executable (Linux)**
<br>
<code>chmod +x scraper.py</code>
<br>
<br>
**Step 4: Run the Script**
<br>
<code>python3 scraper.py</code>

### Output:

At this point the highest amount in USD is printed to the terminal, I also added a feature that the highest amount in saved inside a <code>results.json</code> file where the date is sorted per date. By having this file you can select the highest trades on a specific day if you would like.
<br>
<br>
**Json Output Format:**
<br>

```
{
	"yyyy-mm-dd": [
		{
			"Hash" : "hash is here",
			"Time": "Time of transaction",
			"Amount (BTC)": "Amount of BTC",
			"Amount (USD)": "Amount in USD"
		}
	]
}
```

## Task 2: MongoDB

The next objective is to save the highest BTC transaction to a [MongoDB](https://www.mongodb.com/) collection. In order to accomplish this objective you need to download and install MongoDB. As we are using an ubuntu virtual machine, this is quite easy by using the terminal.

### Installation (Follow these steps or just run setup_mongo.sh)

**Step 1: Install MongoDB**
<br>
<code>
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
</code>
<br>
<br>
<code>
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
</code>
<br>
<br>
<code>sudo apt-get install -y mongodb-org</code>
<br>
<br>
**Step 2: Import python package**
<br>
If you didnt install all the python packages required for this project mentioned in Task 1 (Installed using requirements.txt file), you need to install the python package for mongodb manually.
<br>
<code>pip3 install pymongo</code>
<br>
<br>
**Step 3: Start MongoDB Service**
<br>
<code>sudo systemctl start mongod</code>

### Usage:

For task 1 you had to run the <code>scraper.py</code> file to execute the scraper, in this part of the assignment I chanced it up a little bit. I created a file called <code>main.py</code>. From now on, the only file you need to run is <code>main.py</code> to use this project. As mentioned before you need to make this file executable in order to use it.<br>
<br>(Reminder)<br>
**Step 1: Clone my repository**
<br>
<code>git clone https://github.com/yorickcleerbout/Databases-Advanced.git</code>
<br>
<br>
**Step 2: Install required python packages**
<br>
<code>pip3 install -r requirements.txt</code>
<br>
<br>
**Step 3: Make the python script executable (Linux)**
<br>
<code>chmod +x main.py</code>
<br>
<br>
**Step 4: Run the Script**
<br>
<code>python3 main.py</code>

## Task 3: Redis

This task is all about the availability of the data during execution, Redis is a key-value paired database that I'm using to cache my scraped data temperary. The way I implemented Redis is after i scrape the data I immediatly "save" the data in a Redis database that holds the information for about 1 minute, when the data is in Redis my `parser.py` file gets the data out of Redis to filter for the highest value to be able to save this into a MongoDB.

## Installation (Follow these steps or just run setup_redis.sh)

**Step 1: Install Redis**
<br>
<code>sudo apt install redis-server</code>
<br>
<br>
**Step 2: Import python package**
<br>
If you didnt install all the python packages required for this project mentioned in Task 1 (Installed using requirements.txt file), you need to install the python package for redis manually.
<br>
<code>pip3 install redis</code>
<br>
<br>
**Step 3: Start Redis Service**
<br>
<code>sudo systemctl start redis</code>

### Usage:

As always just run the file `main.py` to use the full project.

## Task 4: Docker

For the last part of this assignment we had to transform our project into containers so we can run every single component in a docker container. What this does is, it makes it possible to run this project everywhere you want, the only thing you have to do is install docker (Windows, Linux or MacOS) and start the program.

## Installation of Docker

### Windows & MacOS

`https://www.docker.com/products/docker-desktop`

### Linux

`sudo apt install docker.io`

## Building Docker containers

You can pull my created images from my docker hub profile or you can create your own images using Dockerfiles.

### Pull my images

Scraper: `https://hub.docker.com/repository/docker/yorickcleerbout/scraper`<br>
Parser: `https://hub.docker.com/repository/docker/yorickcleerbout/parser`<br>

### Create your own images

Put the next code in a file with name `Dockerfile` and no extension or download my dockerfiles from this repository.

**Scraper**
`
FROM ubuntu:latest AS scraper
MAINTAINER yorickcleerbout
COPY . .
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN git clone https://github.com/yorickcleerbout/Databases-Advanced.git
RUN cd Databases-Advanced
RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install pandas
RUN pip3 install pymongo
RUN pip3 install redis
RUN cp "Databases-Advanced/DockerVersion/scraper.py" .
CMD ["python3", "scraper.py"]
`<br>
<br>
**Parser**
`
FROM ubuntu:latest AS parser
MAINTAINER yorickcleerbout
COPY . .
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN git clone https://github.com/yorickcleerbout/Databases-Advanced.git
RUN cd Databases-Advanced
RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install pandas
RUN pip3 install pymongo
RUN pip3 install redis
RUN cp "Databases-Advanced/DockerVersion/parser.py" .
CMD ["python3", "parser.py"]
`
