# Databases Advanced

This repository is made as part of a assignment of the course 'Databases Advanced', the intention of this assignment is to get familiar with services like MongoDB, Docker, Virtual Machines etc. To keep this assignment clear and easy to understand we splitted this task in multiple smaller tasks.

## Python Webscraper

The first task is to scrape the [Blockcain website](https://www.blockchain.com/btc/unconfirmed-transactions) for all the current [Bitcoin (BTC)](https://nl.wikipedia.org/wiki/Bitcoin) transactions all over the world. The output of this part of the assignment has to be the highest **USD** value at the moment of scraping. When you are running a webscraper permanently it can become quite heavy for your computer thats why I recommend running this in a cloud based environment or virutual machine.

### Usage:

**Step 1: Clone my repository**
<br>
<code>git clone https://github.com/yorickcleerbout/Databases-Advanced.git</code>
<br>
<br>
**Step 2: Install required python packages**
<br>
<code>python -m install requirements.txt</code>
<br>
<br>
**Step 3: Run the Scraper**
<br>
<code>python3 scraper.py</code>
