from fastapi import APIRouter,Depends
from pydantic import BaseModel
from app.core.config import settings
from app.core.dependenies import get_api_key,current_user
from app.services.model_servies import prediction_car_price

router = APIRouter()

class CarFeature(BaseModel):
    company:str
    year : int
    owner : str
    fuel : str
    seller_type : str
    transmission : str
    km_driven : float
    mileage_mpg : float
    engine_cc :float
    max_power_bhp : float
    torque_nm : float
    seats :  float

@router.post("/predict")
def predict(car:CarFeature,user=Depends(current_user), _=Depends(get_api_key)):
    prediction = prediction_car_price(car.model_dump())
    return {"predicted_price":prediction}   