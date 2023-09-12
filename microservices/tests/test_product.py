import pytest
from flask import Flask
from microservices.products import product

@pytest.fixture
def client():
    product.testing = True
    with product.test_client() as client:
        yield client

def test_add_product(client: client, monkeypatch: pytest.MonkeyPatch):
    mock_product_data = {'id': 1, 'name': 'Product 1'}
    
    def mock_add_product(mock_product_data):
        return mock_product_data
    
    monkeypatch.setattr('your_app.db.add_product', mock_add_product)
    
    response = client.post('/add_product', json={'name': 'Product 1'})
    
    assert response.status_code == 200
    assert response.json == {'message': 'Product added successfully.'}

def test_get_product_existing(client: FlaskClient, monkeypatch: MonkeyPatch):
    mock_product_data = {'id': 1, 'name': 'Product 1'}
    
    def mock_get_product(product_id):
        return mock_product_data
    
    monkeypatch.setattr('your_app.db.get_product', mock_get_product)
    
    response = client.get('/get_product/1')
    
    assert response.status_code == 200
    assert response.json == {'id': 1, 'name': 'Product 1'}

def test_get_product_nonexistent(client: FlaskClient, monkeypatch: MonkeyPatch):
    def mock_get_product(product_id):
        return None
    
    monkeypatch.setattr('your_app.db.get_product', mock_get_product)
    
    response = client.get('/get_product/999')
    
    assert response.status_code == 404
    assert response.json == {'error': 'Product not found.'}

def test_delete_product_existing(client: FlaskClient, monkeypatch: MonkeyPatch):
    def mock_delete_product(product_id):
        return True
    
    monkeypatch.setattr('your_app.db.delete_product', mock_delete_product)
    
    response = client.delete('/delete_product/1')
    
    assert response.status_code == 200
    assert response.json == {'message': 'Product deleted successfully.'}

def test_delete_product_nonexistent(client: FlaskClient, monkeypatch: MonkeyPatch):
    def mock_delete_product(product_id):
        return False
    
    monkeypatch.setattr('your_app.db.delete_product', mock_delete_product)
    
    response = client.delete('/delete_product/999')
    
    assert response.status_code == 404
    assert response.json == {'error': 'Product not found.'}