#!/bin/sh
# wait-for-postgres.sh

until pg_isready -h db -p 5432 -U user; do
  echo "Czekam na PostgreSQL..."
  sleep 2
done

exec "$@"
