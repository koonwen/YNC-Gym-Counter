import pytest
from flask import g, session
from app.db.models import Admin


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_register(client, app):
    assert client.get('/register').status_code == 200
    response = client.post(
        '/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers['Location'] == 'http://localhost/login'
    with app.app_context():
        assert Admin.verify(username='a', password='a') is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('a', 'test', b'Incorrect username.'),
        ('test', 'a', b'Incorrect password.')
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_login(client, auth):
    assert client.get('/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == 'http://localhost/admin/'

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user.username == 'test'


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
