#!/bin/bash
set -e

# Load variables from .env file (if present)
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "Starting FastAPI with Uvicorn..."

# Wait for DB (optional, basic check)
until (echo > /dev/tcp/db/5432) 2>/dev/null; do
  echo "⏳ Waiting for database..."
  sleep 1
done
echo "✅ Database is up!"

exec uvicorn app.main:app --host "$APP_HOST" --port "$APP_PORT" --reload
