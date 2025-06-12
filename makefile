build:  ; docker build -t cluster-apache-spark:3.5.3 .

build-nc: ; docker-compose build --no-cache

build-progress: ; docker-compose build --no-cache --progress=plain

down: ; docker-compose down

up: ; docker-compose up -d

run-scaled: ; make down && docker-compose up --scale spark-worker=3

run-d: ; make down && docker-compose up -d

stop: ; docker-compose stop

init: ; colima start --mount /Users/richardwieland/Desktop/projects:w --cpu 6 --memory 6

start: ; make down &&  make build && docker-compose up -d

submit: ;  docker exec  -w /opt -i -t spark_optimizer-spark-master-1 ./spark/bin/spark-submit  --master spark://spark-master:7077 \
--driver-memory 1G \
--executor-memory 1G \
--packages io.delta:delta-spark_2.12:3.3.0 ./apps/data_generator/main.py