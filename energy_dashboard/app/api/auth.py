from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import response

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
        raise HTTPException(status_code=401)

    token = create_access_token(user["username"])

    # cookie HTTP-only (ważne!)
    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        samesite="strict"
    )

    return {"ok": True}
