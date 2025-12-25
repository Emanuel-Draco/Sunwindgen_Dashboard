from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from api.auth import router as auth_router
from api.energy import router as energy_router

app = FastAPI()

# ===== STATIC FILES =====
app.mount("/static", StaticFiles(directory="static"), name="static")

# ===== ROUTERS =====
app.include_router(auth_router, prefix="/api")
app.include_router(energy_router, prefix="/api")

# ===== PAGES =====
@app.get("/")
def login_page():
    return FileResponse("static/login.html")

@app.get("/dashboard.html")
def dashboard():
    return FileResponse("static/dashboard.html")

@app.get("/history.html")
def history():
    return FileResponse("static/history.html")

@app.get("/settings.html")
def settings():
    return FileResponse("static/settings.html")
