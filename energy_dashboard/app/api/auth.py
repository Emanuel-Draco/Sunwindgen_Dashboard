# app/auth.py
from fastapi import APIRouter, HTTPException, Depends, Response
from pydantic import BaseModel
from auth.users import get_user
from auth.security import verify_password, create_access_token, get_current_user

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest, response: Response):
    user = get_user(data.username)
    if not user or not verify_password(data.password, user["password_hash"]):
        raise HTTPException(status_code=401)

    token = create_access_token(user["username"])

    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        samesite="strict"
    )

    return {"ok": True}

@router.get("/verify")
def verify(current_user: str = Depends(get_current_user)):
    # Endpoint pomocniczy do weryfikacji tokenu
    return {"username": current_user}
