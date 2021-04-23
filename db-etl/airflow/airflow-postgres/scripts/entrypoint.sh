#entrypoint.sh

#!/usr/bin/env bash
airflow initdb
airflow webserver