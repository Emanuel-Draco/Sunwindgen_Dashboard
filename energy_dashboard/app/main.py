from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.auth import router as auth_router
from api.energy import router as energy_router
from api.health import router as health_router

app = FastAPI(title="Energy Dashboard")

# =========================================================
# Pomocnicza funkcja – HTML bez cache (KLUCZOWE!)
# =========================================================
def no_cache_response(path: str):
    response = FileResponse(path)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# =========================================================
# API
# =========================================================
app.include_router(auth_router, prefix="/api")
app.include_router(energy_router, prefix="/api")
app.include_router(health_router, prefix="/api")

# =========================================================
# HTML ROUTES (login + dashboard + podstrony)
# =========================================================
@app.get("/")
def login_page():
    return no_cache_response("static/login.html")

@app.get("/dashboard.html")
def dashboard_page():
    return no_cache_response("static/dashboard.html")

@app.get("/history.html")
def history_page():
    return no_cache_response("static/history.html")

@app.get("/settings.html")
def settings_page():
    return no_cache_response("static/settings.html")

# =========================================================
# Static files (JS, CSS)
# =========================================================
app.mount("/static", StaticFiles(directory="static"), name="static")
