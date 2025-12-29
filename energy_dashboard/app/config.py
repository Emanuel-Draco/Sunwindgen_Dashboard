import json
from pathlib import Path

OPTIONS_PATH = Path("/data/options.json")

def load_options() -> dict:
    if not OPTIONS_PATH.exists():
        raise RuntimeError("options.json not found")
    return json.loads(OPTIONS_PATH.read_text())

options = load_options()

SECRET_KEY = options.get("secret_key")
if not SECRET_KEY:
    raise RuntimeError("secret_key missing in options.json")
