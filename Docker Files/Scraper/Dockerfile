FROM ubuntu:latest AS Scraper
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

