#!/bin/sh

# Set default values if env vars are not provided
HOST="${DB_HOST:-postgres}"
PORT="${DB_PORT:-5432}"

echo "Waiting for postgres at $HOST:$PORT..."

# Wait until postgres is available
while ! nc -z $HOST $PORT; do
  sleep 1
done

echo "PostgreSQL started"

# Run the Django command passed in CMD
exec "$@"
