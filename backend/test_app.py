from starlette.testclient import TestClient

from app import app

client = TestClient(app)

def test_list_cities_empty():
    response = client.get('/cities/')
    assert response.status_code == 200
    assert response.json() == []


def test_list_cities():
    response = client.post('/cities/', json={'name':'Blumenau'})
    assert response.status_code == 201

    response = client.get('/cities/')
    assert response.status_code == 200
    cities =  response.json()
    assert len(cities) > 0
    assert cities[0]['name'] == 'Blumenau'.lower()