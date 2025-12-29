import json
from pathlib import Path

OPTIONS_PATH = Path("/data/options.json")

if not OPTIONS_PATH.exists():
    raise RuntimeError("options.json not found")

options = json.loads(OPTIONS_PATH.read_text())

SECRET_KEY = options.get("secret_key")

if not SECRET_KEY:
    raise RuntimeError("secret_key missing in options.json")
