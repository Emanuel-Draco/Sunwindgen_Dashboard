from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from auth.users import get_user
from auth.security import verify_password, create_access_token
from config import SECRET_KEY

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest, response: Response):
    print("LOGIN ATTEMPT:", data.username)

    user = get_user(data.username)
    print("USER:", user)

    if not user:
        print("NO SUCH USER")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    ok = verify_password(data.password, user["password_hash"])
    print("PASSWORD OK:", ok)

    if not ok:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user["username"])
    print("TOKEN CREATED")

    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        samesite="strict",
        secure=False
    )

    return {"ok": True}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("session")
    return {"ok": True}