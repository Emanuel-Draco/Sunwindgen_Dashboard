from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.auth import router as auth_router
from api.energy import router as energy_router
from auth.security import verify_token

app = FastAPI()
security = HTTPBearer()

# STATIC
app.mount("/static", StaticFiles(directory="static"), name="static")

# API
app.include_router(auth_router, prefix="/api")
app.include_router(energy_router, prefix="/api")

# LOGIN (PUBLIC)
@app.get("/")
def login_page():
    return FileResponse("static/HTML/login.html")

# PROTECTED PAGES
@app.get("/dashboard.html")
def dashboard(credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials.credentials)
    return FileResponse("static/HTML/dashboard.html")

@app.get("/history.html")
def history(credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials.credentials)
    return FileResponse("static/HTML/history.html")

@app.get("/settings.html")
def settings(credentials: HTTPAuthorizationCredentials = Depends(security)):
    verify_token(credentials.credentials)
    return FileResponse("static/HTML/settings.html")
