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


def test_create_team(client):
    response = client.post('/teams/', json=PAYLOAD_TEAM)
    assert response.status_code == 201

def test_get_all_teams(client):
    client.post('/teams/', json=PAYLOAD_TEAM)

    response = client.get('/teams/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1 

def test_get_team_by_id(client):
    post_response = client.post('/teams/', json=PAYLOAD_TEAM)
    team_id = post_response.get_json()['id']

    response = client.get(f'/teams/{team_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == team_id

def test_update_team(client):
    post_response = client.post('/teams/', json=PAYLOAD_TEAM)
    team_id = post_response.get_json()['id']

    updated_data = PAYLOAD_TEAM_UPDATE
    response = client.put(f'/teams/{team_id}', json=updated_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == updated_data['name']

def test_patch_team(client):
    post_response = client.post('/teams/', json=PAYLOAD_TEAM)
    team_id = post_response.get_json()['id']

    patch_data = {"country": "Belgium"}
    response = client.patch(f'/teams/{team_id}', json=patch_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['country'] == "Belgium"

def test_delete_team(client):
    post_response = client.post('/teams/', json=PAYLOAD_TEAM)
    team_id = post_response.get_json()['id']

    response = client.delete(f'/teams/{team_id}')
    assert response.status_code == 204

    get_response = client.get(f'/teams/{team_id}')
    assert get_response.status_code == 404