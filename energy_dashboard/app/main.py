from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.health import router as health_router
from api.energy import router as energy_router
from api.auth import router as auth_router

app = FastAPI(title="Energy Dashboard")

# API
app.include_router(auth_router, prefix="/api")
app.include_router(health_router, prefix="/api")
app.include_router(energy_router, prefix="/api")

@app.get("/")
def root():
    return FileResponse("static/login.html")

@app.get("/dashboard.html")
def dashboard():
    return FileResponse("static/dashboard.html")

@app.get("/history.html")
def history_page():
    return FileResponse("static/history.html")

@app.get("/settings.html")
def settings_page():
    return FileResponse("static/settings.html")

app.mount("/static", StaticFiles(directory="static"), name="static")
