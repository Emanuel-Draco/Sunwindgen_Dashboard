from auth.security import hash_password

users_db = {
    "admin": {
        "username": "admin",
        "password_hash": hash_password("admin123")
    }
}

def get_user(username: str):
    return users_db.get(username)
