import os 
from dotenv import load_dotenv
load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Project"
    API_KEY: str = os.getenv("API_KEY")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    REDIS_URL: str = os.getenv("REDIS_URL")
    JWT_ALGORITHM: str = "HS256"
    MODELS_PATH: str = "app/models/model.joblib"

settings = Settings()