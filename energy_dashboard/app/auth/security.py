# app/security.py
from jose import jwt, JWTError
from fastapi import Request, HTTPException, Header
from datetime import datetime, timedelta
import hashlib

SECRET_KEY = "CHANGE_ME_IN_STAGE_3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash

def create_access_token(subject: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(request: Request, authorization: str = Header(None)):
    # Pobierz token z nagłówka Authorization (Bearer) lub z ciasteczka
    token = None
    if authorization:
        scheme, _, param = authorization.partition(" ")
        if scheme.lower() != "bearer" or not param:
            raise HTTPException(status_code=401, detail="Nieprawidłowy nagłówek autoryzacji")
        token = param
    else:
        token = request.cookies.get("session")
    if not token:
        raise HTTPException(status_code=401, detail="Nieautoryzowany")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Nieprawidłowy lub wygasły token")
