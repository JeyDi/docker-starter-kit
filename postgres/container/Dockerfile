FROM postgres:alpine

RUN mkdir -p /home/data/backup/
RUN mkdir -p /home/data/query/

COPY init.sql /docker-entrypoint-initdb.d/
