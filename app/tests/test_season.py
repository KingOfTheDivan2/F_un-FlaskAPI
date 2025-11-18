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

def test_create_season(client):
    response = client.post('/seasons/', json=PAYLOAD_SEASON)
    assert response.status_code == 201

def test_get_all_seasons(client):
    client.post('/seasons/', json=PAYLOAD_SEASON)

    response = client.get('/seasons/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1

def test_get_season_by_id(client):
    post_response = client.post('/seasons/', json=PAYLOAD_SEASON)
    season_id = post_response.get_json()['id']

    response = client.get(f'/seasons/{season_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == season_id

def test_update_season(client):
    post_response = client.post('/seasons/', json=PAYLOAD_SEASON)
    season_id = post_response.get_json()['id']

    updated_data = PAYLOAD_SEASON_UPDATE
    response = client.put(f'/seasons/{season_id}', json=updated_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['year'] == updated_data['year']

def test_patch_season(client):
    post_response = client.post('/seasons/', json=PAYLOAD_SEASON)
    season_id = post_response.get_json()['id']
    patch_data = {"is_current": False}
    response = client.patch(f'/seasons/{season_id}', json=patch_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['is_current'] == False

def test_delete_season(client):
    post_response = client.post('/seasons/', json=PAYLOAD_SEASON)
    season_id = post_response.get_json()['id'] 

    response = client.delete(f'/seasons/{season_id}')
    assert response.status_code == 204

    get_response = client.get(f'/seasons/{season_id}')
    assert get_response.status_code == 404
