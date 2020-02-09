from starlette.testclient import TestClient

from app import app

client = TestClient(app)

def test_list_cities_empty():
    response = client.get('/cities/')
    assert response.status_code == 200
    assert response.json() == []


def test_add_cities():
    response = client.post('/cities/', json={'name':'Blumenau'})
    assert response.status_code == 201


def test_list_cities_one_element():
    response = client.get('/cities/')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_city_by_id():
    response = client.get('/cities/')
    id = response.json()[0]['id']

    response = client.get('/cities/' + id)
    assert response.json()['id'] == id