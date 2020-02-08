import os
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from uuid import uuid4
from datetime import datetime

database_string = os.getenv('APP_DATABASE', default = 'MEMORY')

if database_string == 'MEMORY':
    db = TinyDB(storage=MemoryStorage)
else:
    db = TinyDB(database_string + '.json')


cities = db.table('cities')


def insert_city(city_name, city_api_id, forecast):
    id = str(uuid4())
    cities.insert({'id':id, 'name': city_name.lower(), 'timestamp': datetime.utcnow().isoformat(), 'api_id':city_api_id, 'forecast': forecast})
    return get_city(id)


def exists_city(city_name):
    City = Query()
    return cities.search(City.name == city_name.lower())


def get_city(city_id):
    City = Query()
    try:
        return cities.search(City.id == city_id)[0]
    except:
        pass


def fetch_cities():
    return cities.all()


def update_forecast(city_id, forecast):
    city = get_city(city_id)
    now  = datetime.utcnow()
    last = datetime.datetime.strptime(city['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    if (now - last).days >= 1:
        city.forecast = forecast
        cities.write_back(city)
        return city