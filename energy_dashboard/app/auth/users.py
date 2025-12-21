# app/auth/users.py

users_db = {
    "admin": {
        "username": "admin",
        # hasło: admin123
        "password_hash": "$2b$12$KIXQ0r3kYkY7Z8wKZ4ZQ0uQZ8z5zHhZ8f8Yf3d7K6N5G9H4C2E3S"
    }
}

def get_user(username: str):
    return users_db.get(username)
