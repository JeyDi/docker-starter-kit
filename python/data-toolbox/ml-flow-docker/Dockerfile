
FROM python:3.7.0

RUN pip install mlflow
RUN pip install psycopg2

EXPOSE 5042

RUN mkdir -p /server
WORKDIR /server
COPY . /server

RUN chmod +x wait-for-it.sh

RUN mkdir /mlflow/

CMD ./wait-for-it.sh postgres:5442 -- mlflow server \
    --backend-store-uri postgresql://admin:secret@postgres:5442/mlflow \
    --default-artifact-root /mlflow \
    --host 0.0.0.0