from datetime import datetime


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


def test_pi_route(client):
    response = client.post('admin/pi', json={"timestamp": str(datetime.now()),
                                        "img1": 1,
                                        "img2": 1,
                                        "img3": 3,
                                        "img4": 2,
                                        "img5": 5,
                                        "mode": 3}
                           )
    assert response.status_code == 200
    assert response.data == b'Success'