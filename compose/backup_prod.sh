#!/bin/bash
# ##############################################################
# Este comando hace un backup de la instancia de produccion
# Se usa en un crontab para ejecutar el backup diario
# logea el job en /var/log/backup_prod.log
# ##############################################################

set -e

# incluir las variables comunes excluyendo las de dockerfile
source <(grep -v '^#' .env | grep -v 'Host(')


# --------------------------------------------------------------------------------------
# Hacer un backup de la base de produccion
# --------------------------------------------------------------------------------------
sudo docker run --rm \
    --network compose_default \
    --volume ${base_ar}:/base \
    --link postgres:db \
    ${DBTOOLS_IMAGE} --days-to-keep ${days_to_keep} \
        --backup

