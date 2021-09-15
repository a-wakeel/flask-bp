#!/usr/bin/env bash
# entrypoint script for postgres server
set -e

if [[ "$1" = 'postgres' ]]; then
    mkdir -p /data/config
    mkdir -p /data/db
    chown -R postgres.postgres /data
    chmod 700 /data
    chmod 700 /data/config
    chmod 700 /data/db

    mkdir -p /run/postgresql
    chmod g+s /run/postgresql
    chown -R postgres /run/postgresql

    if [[ ! -f "/data/config/postgresql.conf" ]]; then
        echo "Copying default postgresql.conf since no copy exists in volume"
        cp /etc/db_config/postgresql.conf /data/config/postgresql.conf

        if [[ ! -z ${DB_ENABLE_AUTO_EXPLAIN} ]] && [[ ${DB_ENABLE_AUTO_EXPLAIN} = 1 ]]; then
            echo "Enabling auto_explain feature"
            if grep -q "shared_preload_libraries" /data/config/postgresql.conf; then
                sed -ri "s/(shared_preload_libraries)\s*=\s*['\"]([^'\"]*)['\"]/\1='\2,auto_explain'/" /data/config/postgresql.conf
            else
                echo "shared_preload_libraries = 'auto_explain'" >> /data/config/postgresql.conf
            fi

            echo "auto_explain.log_min_duration = '10s'" >> /data/config/postgresql.conf
            echo "auto_explain.log_nested_statements = on" >> /data/config/postgresql.conf
        fi

        if [[ ! -z ${DB_TRACK_IO_TIMING} ]] && [[ ${DB_TRACK_IO_TIMING} = 1 ]]; then
            echo "Enabling track_io_timing feature"
            echo "track_io_timing = on" >> /data/config/postgresql.conf
        fi

        chown postgres.postgres /data/config/postgresql.conf
    fi

    if [[ ! -f "/data/config/pg_hba.conf" ]]; then
        echo "Copying default pg_hba.conf since no copy exists in volume"
        cp /etc/db_config/pg_hba.conf /data/config/pg_hba.conf
        chown postgres.postgres /data/config/pg_hba.conf
    fi

    if [[ ! -f "/data/config/pg_ident.conf" ]]; then
        echo "Copying default pg_ident.conf since no copy exists in volume"
        cp /etc/db_config/pg_ident.conf /data/config/pg_ident.conf
        chown postgres.postgres /data/config/pg_ident.conf
    fi

    if [[ ! -s "/data/db/PG_VERSION" ]]; then
        echo
        echo 'No PostgreSQL DB found in /data/db. Creating new cluster...'
        echo
        gosu postgres initdb -D /data/db

        echo
        echo 'Deleting configuration created by initdb - using config in /data/config instead'
        echo
        gosu postgres rm /data/db/postgresql.conf
        gosu postgres rm /data/db/pg_hba.conf
        gosu postgres rm /data/db/pg_ident.conf

        echo
        echo 'PostgreSQL cluster creation complete'
        echo

        if [[ ! -z ${DB_ROOT_USER} ]]; then
            echo
            echo 'Starting local-only PostgreSQL server so that database root user can be created '
            echo
            gosu postgres pg_ctl -D /data/db \
                -o "-c listen_addresses='localhost' -c config_file='/data/config/postgresql.conf'" \
                -w start

            if [[ ! -z ${DB_ROOT_PASSWORD} ]]; then
                echo
                echo 'Creating PostgreSQL root user for creating databases and roles'
                echo
                gosu postgres psql -v ON_ERROR_STOP=1 -c \
                    "CREATE USER ${DB_ROOT_USER} WITH SUPERUSER LOGIN ENCRYPTED PASSWORD '${DB_ROOT_PASSWORD}';"
            else
                echo
                echo 'Creating PostgreSQL root user for creating databases and roles (WARNING: NO password set)'
                echo
                gosu postgres psql -v ON_ERROR_STOP=1 -c \
                    "CREATE USER ${DB_ROOT_USER} WITH SUPERUSER LOGIN;"
                echo "DB_ROOT_PASSWORD environment variable not set!"
                echo "--> If not for local development, you should assign a password to the PostgreSQL root user!"
            fi

            echo
            echo 'Stopping local-only PostgreSQL server'
            echo
            gosu postgres pg_ctl -D /data/db -m fast \
                -o "-c config_file='/data/config/postgresql.conf'" \
                -w stop
        else
            echo "DB_ROOT_USER environment variable not set!"
            echo "--> You will need to create a superuser so that databases and roles can be maintained."
            echo "--> This new account should not be used as an application account."""
        fi

        echo
        echo 'New cluster init complete'
        echo
    fi

    exec gosu postgres postgres --config-file=/data/config/postgresql.conf
fi

exec "$@"