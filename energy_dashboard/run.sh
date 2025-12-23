#!/usr/bin/env bash
set -e

echo "Starting Energy Dashboard API"
exec python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
