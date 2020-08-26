#!/usr/bin/env bash

DB_CONTAINER="${1:-django-dashboard-coreui_postgres_1}"
USERNAME="${2:-changeme}"
DATABASE="${3:-asrg}"
APP_CONTAINER="${4:-asrg-app}"

docker exec ${DB_CONTAINER} psql -U ${USERNAME} -d postgres -c "DROP DATABASE ${DATABASE};"
docker exec ${DB_CONTAINER} psql -U ${USERNAME} -d postgres -c "CREATE DATABASE ${DATABASE};"
docker exec ${APP_CONTAINER} python manage.py migrate

