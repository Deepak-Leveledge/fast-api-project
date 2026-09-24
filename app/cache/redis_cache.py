import redis 
import os  
import json
from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)

def get_cache_prediction(key:str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def set_cache_prediction(key:str, value:dict, expire_seconds:int=3600):
    redis_client.setex(key, expire_seconds, json.dumps(value))