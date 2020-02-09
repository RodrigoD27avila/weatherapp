from typing import List
from pydantic import BaseModel

class ForecastResultWeather(BaseModel):
    main: str
    description: str
    icon: str

class ForecastResultMain(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class ForecastCoord(BaseModel):
    lon: float
    lat: float


class ForecastCity(BaseModel):
    id: int
    name: str
    coord: ForecastCoord
    country: str
    timezone: int
    sunrise: int
    sunset: int


class ForecastResult(BaseModel):
    dt: int
    dt_txt: str
    main: ForecastResultMain
    weather: List[ForecastResultWeather]


class Forecast(BaseModel):
    cod: int
    cnt: int
    list: List[ForecastResult]
    city: ForecastCity


class City(BaseModel):
    id: str
    name: str
    forecast: Forecast


class CityName(BaseModel):
    name: str
