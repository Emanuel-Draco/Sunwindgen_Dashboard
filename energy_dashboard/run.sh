#!/usr/bin/with-contenv bash
set -ex

echo "PWD:"
pwd

echo "LS /:"
ls -la /

echo "LS /app:"
ls -la /app

echo "WHICH PYTHON:"
which python3

echo "RUNNING PYTHON VERSION:"
python3 --version

echo "TRY IMPORT:"
python3 - << 'EOF'
print("PYTHON WORKS")
EOF

echo "START MAIN"
exec python3 /app/main.py
