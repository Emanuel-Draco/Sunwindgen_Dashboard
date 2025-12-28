from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from api.auth import router as auth_router
from api.energy import router as energy_router
from auth.security import get_current_user
from pathlib import Path

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

@app.get("/")
def login_page(user=Depends(get_current_user)):
    return RedirectResponse("/dashboard.html")

@app.get("/login")
def login_fallback():
    return FileResponse(FRONTEND_DIR / "login.html")

@app.get("/dashboard.html")
def dashboard(user=Depends(get_current_user)):
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