#!/usr/bin/env bash

DB_CONTAINER="${1:-asrg-postgres}"
USERNAME="${2:-changeme}"
DATABASE="${3:-asrg}"
PATH="${3:-~/database_backups}"

docker exec -t ${DB_CONTAINER} pg_dumpall -c -U ${USERNAME} > ${PATH}/asrg_`date +%d-%m-%Y"_"%H_%M_%S`.sql

