from datetime import datetime

from fastapi import FastAPI, HTTPException

from starlette.middleware.cors import CORSMiddleware    
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_303_SEE_OTHER, HTTP_404_NOT_FOUND

from typing import List
import models
import database
import weather

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5000",
    "http://54.156.242.55",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/cities/', response_model=List[models.City], status_code=HTTP_200_OK)
async def list_all_cities():
    return database.fetch_cities()


@app.post('/cities/', response_model=models.City, status_code=HTTP_201_CREATED)
async def insert_city(city: models.CityName):
    if not database.exists_city(city.name):
        status_code, forecast = weather.exists_city(city.name)
        if status_code == HTTP_200_OK and forecast['cod'] != '404':
            result = database.insert_city(city.name, city_api_id=forecast['city']['id'], forecast=forecast)
            return models.City(**result)
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="A cidade de {} não existe.".format(city.name))
    raise HTTPException(status_code=HTTP_303_SEE_OTHER, detail="Cidade já registrada.")


@app.get('/cities/{city_id}', response_model=models.City, status_code=HTTP_200_OK)
async def update_forecast_cache(city_id):
    city = database.get_city(city_id)
    if (city is None):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Não foi possível encontrar a cidade com o id {}".format(city_id))   
    
    city_api_id = city['api_id']
    now  = datetime.utcnow()
    last = datetime.fromisoformat(city['timestamp'])
    if (now - last).days >= 1:
        city['forecast'] = weather.forecast(city_api_id)
        cities.write_back(city)
    return database.get_city(city_id)
    
