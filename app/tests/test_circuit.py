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


def test_create_circuit(client):
    response = client.post('/circuits/', json=PAYLOAD_CIRCUIT)
    assert response.status_code == 201

def test_get_all_circuits(client):
    # First, create a circuit to ensure there is data to retrieve
    client.post('/circuits/', json=PAYLOAD_CIRCUIT)
    
    response = client.get('/circuits/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1  # At least one circuit should be present

def test_get_circuit_by_id(client):
    # First, create a circuit to retrieve
    post_response = client.post('/circuits/', json=PAYLOAD_CIRCUIT)
    circuit_id = post_response.get_json()['id']
    
    response = client.get(f'/circuits/{circuit_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == circuit_id

def test_update_circuit(client):
    # First, create a circuit to update
    post_response = client.post('/circuits/', json=PAYLOAD_CIRCUIT)
    circuit_id = post_response.get_json()['id']
    
    updated_data = PAYLOAD_CIRCUIT_UPDATE
    response = client.put(f'/circuits/{circuit_id}', json=updated_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == updated_data['name']

def test_patch_circuit(client):
    # First, create a circuit to patch
    post_response = client.post('/circuits/', json=PAYLOAD_CIRCUIT)
    circuit_id = post_response.get_json()['id']
    
    patch_data = {"city": "Monaco"}
    response = client.patch(f'/circuits/{circuit_id}', json=patch_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['city'] == "Monaco"

def test_delete_circuit(client):
    # First, create a circuit to delete
    post_response = client.post('/circuits/', json=PAYLOAD_CIRCUIT)
    circuit_id = post_response.get_json()['id']
    
    response = client.delete(f'/circuits/{circuit_id}')
    assert response.status_code == 204
    
    # Verify deletion
    get_response = client.get(f'/circuits/{circuit_id}')
    assert get_response.status_code == 404