import pytest

from app import app


def test_app_1():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200


def test_app_2():
    response = app.test_client().get('/api/posts')
    assert len(response.json) == 8


def test_app_3():
    response = app.test_client().get('/api/posts/5')
    assert response.json.get("poster_name") == "leo", "Имя получено неверно"


def test_app_4():
    response = app.test_client().get('/api/posts/5')
    assert response.status_code == 200
