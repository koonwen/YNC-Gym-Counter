from flaskr.db import get_db


def test_index(app, client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b"5" in response.data

