FROM python:3.8
WORKDIR /sreality
COPY . .

RUN apt-get update &&apt-get upgrade -y&& apt-get install python3-pip -y && pip3 install psycopg2 && pip3 install psycopg2-binary
RUN pip3 install --upgrade pip
RUN pip3 install cryptography
RUN pip3 install scrapy --upgrade

EXPOSE 80
EXPOSE 5432/tcp
# CMD ["scrapy", "crawl", "sreality"]
CMD ["./wait-for-it.sh" , "db:5432" , "--strict" , "--timeout=300" , "--" , "scrapy", "crawl", "sreality"]
