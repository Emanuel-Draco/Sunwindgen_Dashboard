#!/usr/bin/with-contenv bash
set -e

echo "Starting Energy Dashboard (appliance mode)"

exec python3 /app/main.py
