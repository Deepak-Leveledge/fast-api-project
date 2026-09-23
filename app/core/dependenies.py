from fastapi import Depends,Header,HTTPException,status
from app.core.config import settings
from app.core.security import verify_token



def get_api_key(api_key:str=Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key"
        )
    return api_key


def current_user(token:str= Header(...)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    return payload