#!/usr/bin/env bash

if [ "$#" -ne 1 ]
then
      echo "Usage: bash postgres_restore_backup.sh BACKUP_FILE DB_CONTAINER USERNAME DATABASE"
        exit 1
fi

BACKUP_FILE="${1}"
DB_CONTAINER="${2:-asrg-postgres}"
USERNAME="${3:-changeme}"
DATABASE="${4:-asrg}"

cat ${BACKUP_FILE} | docker exec -i ${DB_CONTAINER} psql -U ${USERNAME}
