from fastapi import APIRouter, Depends
import os

from auth.security import get_current_user

router = APIRouter()

MOCK_MODE = os.environ.get("MOCK_MODE", "true") == "true"

@router.get("/energy")
def energy(user=Depends(get_current_user)):
    if MOCK_MODE:
        return {
            "pv_production": 4200,
            "battery": 78,
            "load": 2600
        }

    return {
        "pv_production": None,
        "battery": None,
        "load": None
    }
