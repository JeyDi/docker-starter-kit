# Restore a Postgres backup

#change this parameters
CONTAINER_NAME=db
DB_HOSTNAME=personal
DB_USER=admin
#change the name of the backup
BACKUP_NAME=dump_12-11-2020_12_18_22.sql

DOCKER_DB_NAME="$(docker-compose ps -q ${CONTAINER_NAME})"
LOCAL_DUMP_PATH="./backup/${BACKUP_NAME}"

#not much safe because use the cat command
#cat ${LOCAL_DUMP_PATH} | docker exec -i ${DOCKER_DB_NAME} psql -U ${DB_USER} -d ${DB_HOSTNAME}

#much more safe (using copying functionalities)
docker cp ${LOCAL_DUMP_PATH} ${DOCKER_DB_NAME}:/home/${BACKUP_NAME}
docker exec -i ${DOCKER_DB_NAME} psql -U ${DB_USER} -d ${DB_HOSTNAME} -f /home/${BACKUP_NAME}



#docker exec -i "${DOCKER_DB_NAME}" pg_restore -C --clean --no-acl --no-owner -U "${DB_USER}" -d "${DB_HOSTNAME}" < "${LOCAL_DUMP_PATH}"

