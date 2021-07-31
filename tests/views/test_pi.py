from datetime import datetime
from base64 import b64encode

def test_pi_route(client):
    wrong_credentials = b64encode(b"wrong_user:wrong_pw").decode('utf-8')
    response = client.post('/pi/data', headers={"Authorization":f"Basic {wrong_credentials}"})
    assert response.status_code == 401

    credentials = b64encode(b"test_user:test_pw").decode('utf-8')
    response = client.post('/pi/data',
                           headers={"Authorization": f"Basic {credentials}"},
                           json={"timestamp": str(datetime.now()),
                                        "img1": 1,
                                        "img2": 1,
                                        "img3": 3,
                                        "img4": 2,
                                        "img5": 5,
                                        "mode": 3}
                           )
    assert response.status_code == 200
    assert response.data == b'Success'
