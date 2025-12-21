from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.health import router as health_router
from api.energy import router as energy_router

app = FastAPI(title="Energy Dashboard")

# API
app.include_router(health_router, prefix="/api")
app.include_router(energy_router, prefix="/api")

# Frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")
