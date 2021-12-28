#exec a sql script inside container

#change this parameters
CONTAINER_NAME=db
DB_HOSTNAME=personal
DB_USER=admin
SCRIPT="script.sql"

DOCKER_DB_NAME="$(docker-compose ps -q ${CONTAINER_NAME})"

#Copying the file into the volume (more safe)
docker cp './'${SCRIPT} ${DOCKER_DB_NAME}:/home/
docker exec -i ${DOCKER_DB_NAME} psql -U ${DB_USER} -d ${DB_HOSTNAME} -f /home/${SCRIPT}

#Copying content of the file with cat (less safe)
#cat ./${SCRIPT} | docker exec -i ${DOCKER_DB_NAME} psql -U ${DB_USER} -d ${DB_HOSTNAME}