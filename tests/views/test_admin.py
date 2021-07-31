def test_admin(auth, client):
    response = client.get('/admin', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

    auth.login()
    response = client.get('/admin', follow_redirects=True)
    assert response.status_code == 200
    assert b'Logged in as:' in response.data
    assert b'Logout' in response.data
    assert b'Refresh' in response.data