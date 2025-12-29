from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from auth.users import get_user
from auth.security import verify_password, create_access_token

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest, response: Response):
    user = get_user(data.username)
    if not user or not verify_password(data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user["username"], SECRET_KEY)

    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        samesite="strict",
        secure=False  # true gdy HTTPS
    )

    return {"ok": True}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("session")
    return {"ok": True}