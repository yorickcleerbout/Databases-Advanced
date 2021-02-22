<img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" /><img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/><img alt="Pandas" src="https://img.shields.io/badge/pandas%20-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" /><img alt="MongoDB" src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?&style=for-the-badge&logo=mongodb&logoColor=white"/>

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

### Installation (Follow these steps or just run setup.sh)

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
