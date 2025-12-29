from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from starlette.responses import JSONResponse
from api.auth import router as auth_router
from auth.middleware import auth_middleware
from app.config import SECRET_KEY
from api.energy import router as energy_router
from auth.security import get_current_user, create_access_token
from pathlib import Path
import os

SECRET_KEY = os.environ.get("secret_key")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY not set at startup")

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR / "static"),
    name="static"
)

app.include_router(auth_router, prefix="/api")
app.include_router(energy_router, prefix="/api")
app.middleware("http")(auth_middleware)

@app.get("/")
def login_page(user=Depends(get_current_user)):
    return RedirectResponse("/dashboard.html")

@app.get("/login")
def login_fallback():
    return FileResponse(FRONTEND_DIR / "login.html")

@app.get("/dashboard.html")
def dashboard(user=Depends(lambda req=Depends(): get_current_user(req, SECRET_KEY))):
    return FileResponse(FRONTEND_DIR / "dashboard.html")

@app.get("/history.html")
def history(user=Depends(get_current_user)):
    return FileResponse(FRONTEND_DIR / "history.html")

@app.get("/settings.html")
def settings(user=Depends(get_current_user)):
    return FileResponse(FRONTEND_DIR / "settings.html")

@app.get("/navbar.html")
def navbar():
    return FileResponse(FRONTEND_DIR / "navbar.html")

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    print("Unhandled error:", exc)
    return JSONResponse(status_code=500, content={"detail": "Internal error"})