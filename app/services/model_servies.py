import joblib
import os
import json
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cache_prediction, set_cache_prediction


model = joblib.load(settings.MODELS_PATH)

def prediction_car_price(data:dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cache_prediction(cache_key)
    if cached:
        return cached

    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cache_prediction(cache_key,prediction)
    return prediction