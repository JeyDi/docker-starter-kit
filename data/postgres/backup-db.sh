#Backup DB

#change this parameters
CONTAINER_NAME=db
DB_HOSTNAME=personal
DB_USER=admin
LOCAL_DUMP_PATH="./backup/"

DOCKER_DB_NAME="$(docker-compose ps -q ${CONTAINER_NAME})"

docker exec -t ${DOCKER_DB_NAME} pg_dumpall -c -U ${DB_USER} > ${LOCAL_DUMP_PATH}dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql