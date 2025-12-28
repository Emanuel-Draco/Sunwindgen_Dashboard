from fastapi import Request
from starlette.responses import RedirectResponse
from auth.security import get_current_user

EXCLUDED_PATHS = {"/", "/api/login", "/health", "/static"}

async def auth_middleware(request: Request, call_next):
    path = request.url.path

    if any(path.startswith(p) for p in EXCLUDED_PATHS):
        return await call_next(request)

    try:
        get_current_user(request)
    except:
        return RedirectResponse("/")

    return await call_next(request)
