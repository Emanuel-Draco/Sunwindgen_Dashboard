import os
import requests
from fastapi import APIRouter, HTTPException
from fastapi import Depends
from auth.security import get_current_user

router = APIRouter()

SUPERVISOR_TOKEN = os.environ.get("SUPERVISOR_TOKEN")
HA_API = "http://supervisor/core/api/states"

HEADERS = {
    "Authorization": f"Bearer {SUPERVISOR_TOKEN}",
    "Content-Type": "application/json"
}

@router.get("/energy")
def energy(user=Depends(get_current_user)):
    if not SUPERVISOR_TOKEN:
        raise HTTPException(status_code=500, detail="No supervisor token")

    r = requests.get(HA_API, headers=HEADERS, timeout=5)

    if r.status_code != 200:
        raise HTTPException(status_code=500, detail="HA API error")

    states = r.json()

    def get(entity_id):
        for s in states:
            if s["entity_id"] == entity_id:
                return s["state"]
        return None

    return {
        "pv_production": get("sensor.pv_power"),
        "battery": get("sensor.battery_soc"),
        "load": get("sensor.house_consumption")
    }
