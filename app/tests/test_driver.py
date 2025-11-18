import pytest
from app import create_app, db
from app.configs.config import TestConfig
from app.utils.data_utils import *

@pytest.fixture
def client():
    app = create_app(config_class=TestConfig)

    with app.app_context():
        db.create_all()
        
    with app.test_client() as client:
        yield app.test_client()

    with app.app_context():
        db.session.remove()
        db.drop_all()
    

def test_create_driver(client):
    response = client.post('/drivers/', json=PAYLOAD_DRIVER)
    assert response.status_code == 201

def test_get_all_drivers(client):
    client.post('/drivers/', json=PAYLOAD_DRIVER)

    response = client.get('/drivers/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1

def test_get_driver_by_id(client):
    post_response = client.post('/drivers/', json=PAYLOAD_DRIVER)
    driver_id = post_response.get_json()['id']

    response = client.get(f'/drivers/{driver_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == driver_id

def test_update_driver(client):
    post_response = client.post('/drivers/', json=PAYLOAD_DRIVER)
    driver_id = post_response.get_json()['id']

    updated_data = PAYLOAD_DRIVER_UPDATE
    response = client.put(f'/drivers/{driver_id}', json=updated_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['first_name'] == updated_data['first_name']

def test_patch_driver(client):
    post_response = client.post('/drivers/', json=PAYLOAD_DRIVER)
    driver_id = post_response.get_json()['id']
    patch_data = {"last_name": "Jambon"}
    response = client.patch(f'/drivers/{driver_id}', json=patch_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['last_name'] == "Jambon"

def test_delete_team(client):
    post_response = client.post('/drivers/', json=PAYLOAD_DRIVER)
    driver_id = post_response.get_json()['id']

    response = client.delete(f'/drivers/{driver_id}')
    assert response.status_code == 204

    get_response = client.get(f'/drivers/{driver_id}')
    assert get_response.status_code == 404