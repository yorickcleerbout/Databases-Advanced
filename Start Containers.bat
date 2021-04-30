docker pull yorickcleerbout/scraper
docker pull redis
docker pull yorickcleerbout/parser
docker pull mongo
docker run --name scraper yorickcleerbout/scraper
docker run --name redis redis
docker run --name parser yorickcleerbout/parser
docker run -p 27017:27017 --name mongo mongo
docker network create dba
docker network connect dba scraper
docker network connect dba redis
docker network connect dba parser
docker network connect dba mongo
echo "Done"