import os
import jwt
import time

JWT_SECRET = os.getenv("jwt-secret", "super-secret-key")
JWT_ALGORITHM = "HS256"

def verify_jwt(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM],
        options={"require": ["exp", "sub"]},
    )

def create_jwt(subject: str, role: str) -> str:
    payload = {
        "sub": subject,
        "role": role,
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
