from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'hello world'}  # Asset


def test_html_deve_retornar_ok():
    client = TestClient(app)  # Arrange

    response = client.get('/html')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert (
        response.headers['content-type'] == 'text/html; charset=utf-8'
    )  # Asset


def test_user_deve_retornar_ok():
    client = TestClient(app)  # Arrange

    response = client.get('/user')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': 30,
        'is_admin': False,
    }  # Asset
