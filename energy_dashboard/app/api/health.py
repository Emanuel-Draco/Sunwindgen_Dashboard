from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "auth": bool(os.environ.get("SECRET_KEY")),
        "supervisor": bool(os.environ.get("SUPERVISOR_TOKEN"))
    }
