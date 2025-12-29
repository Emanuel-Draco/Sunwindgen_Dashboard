#!/usr/bin/with-contenv sh
set -e

echo "Starting Energy Dashboard API"
echo "secret_key from HA: ${secret_key}"

export SECRET_KEY="${secret_key}"

exec python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
