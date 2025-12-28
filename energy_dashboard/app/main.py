from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.auth import router as auth_router
from api.energy import router as energy_router
from auth.security import get_current_user

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router, prefix="/api")
app.include_router(energy_router, prefix="/api")

@app.get("/")
def login_page():
    return FileResponse("templates/login.html")

@app.get("/dashboard.html")
def dashboard(user=Depends(get_current_user)):
    return FileResponse("templates/dashboard.html")

@app.get("/history.html")
def history(user=Depends(get_current_user)):
    return FileResponse("templates/history.html")

@app.get("/settings.html")
def settings(user=Depends(get_current_user)):
    return FileResponse("templates/settings.html")
