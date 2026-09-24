import redis 
import os  
import json
from app.core.config import settings
from dotenv import load_dotenv
load_dotenv()

REDIS_URL= os.getenv("REDIS_URL")

redis_client = redis.StrickRedis.from_url(REDIS_URL)

def get_cache_prediction(key:str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None


def set_cache_prediction(key:str, value:dict, expire_seconds:int=3600):
    redis_client.setex(key, expire_seconds, json.dumps(value))