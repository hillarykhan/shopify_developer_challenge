from db import init_db
import pytest
from application import create_app
from models import Img
from db import init_db

@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            init_db(app)
        yield client
    
def test_hello(client):
    """Tests output and status code for the main route"""
    url = '/'
    response = client.get(url)
    assert response.get_data() == b"Let's see some cats!"
    assert response.status_code == 200

def test_get_img_valid_output(client):
    """Tests output for the retrieving a valid image"""
    valid_id = 1
    url = '/' + str(valid_id)
    response = client.get(url)
    img = Img.query.filter_by(id=valid_id).first()
    assert response.get_data() == img.img

def test_get_img_valid_status(client):
    """Tests status code for the retrieving a valid image"""
    valid_id = 1
    url = '/' + str(valid_id)
    response = client.get(url)
    assert response.status_code == 200

def test_get_img_invalid_output(client):
    """Tests output for the retrieving an invalid image"""
    invalid_id = 5
    url = '/' + str(invalid_id)
    response = client.get(url)
    assert response.get_data() == b"There is no image with that id"

def test_get_img_invalid_status(client):
    """Tests status code for the retrieving an invalid image"""
    invalid_id = 5
    url = '/' + str(invalid_id)
    response = client.get(url)
    assert response.status_code == 404
