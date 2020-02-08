import os
import requests

appid = os.getenv('WEATHER_APP_ID')

def exists_city(city_name):
    apibase = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&lang=pt_br'
    if (appid):
        apibase = apibase + '&appid=' + appid

    r = requests.get(apibase)
    return r.status_code, r.json()


def forecast(city_api_id):
    apibase = f'https://api.openweathermap.org/data/2.5/forecast?id={city_api_id}&lang=pt_br'
    if (appid):
        apibase = apibase + '&appid=' + appid

    r = requests.get(apibase)
    return r.status_code, r.json()