from fastapi import APIRouter
from app.core.security import create_token
from pydantic import BaseModel


router = APIRouter()

class AuthInput(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(auth: AuthInput):
    if auth.username == "admin" and auth.password == "password":
        token = create_token({"sub": auth.username})
        return {"access_token": token}
    return {"error": "Invalid credentials"}
