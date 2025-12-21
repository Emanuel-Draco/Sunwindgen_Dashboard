from auth.security import hash_password

users_db = {
    "admin": {
        "username": "admin",
        "password_hash": "$2b$12$3Zp3xwV9Y4xQZqEJk8Vb0uL8sP5mNq..."
    }
}

def get_user(username: str):
    return users_db.get(username)