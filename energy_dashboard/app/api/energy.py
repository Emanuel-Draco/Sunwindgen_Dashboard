import os
import requests
from fastapi import APIRouter, Depends, HTTPException

from auth.security import get_current_user

router = APIRouter()

# domyślnie MOCK włączony
MOCK_MODE = os.environ.get("MOCK_MODE", "true").lower() == "true"

@router.get("/energy")
def energy(user=Depends(get_current_user)):
    if MOCK_MODE:
        return {
            "pv_production": 4200,   # W
            "battery": 78,           # %
            "load": 2600             # W
        }

    # ⬇⬇⬇ JUTRO PODPINAMY PRAWDZIWE ENCJE ⬇⬇⬇
    return {
        "pv_production": None,
        "battery": None,
        "load": None
    }