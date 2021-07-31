import os
import tempfile

import pytest
from app import create_app
from app.db import init_db
from mock_data import load_mock_data
from werkzeug.security import generate_password_hash


@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv('PI_USERNAME', 'test_user')
    monkeypatch.setenv('PI_PASSWORD', generate_password_hash('test_pw'))


@pytest.fixture
def app():
    """Create the application object"""
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:////' + db_path
    })

    with app.app_context():
        init_db()
        load_mock_data()
    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
