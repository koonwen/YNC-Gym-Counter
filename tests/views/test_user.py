from app.db.db_utils import reset_data_table

def test_index(app, client, auth):
    # Test when there is data
    response = client.get('/')
    assert b"12" in response.data
    assert b"2018-01-01 00:00:00" in response.data

    # Test when there is no data
    with app.app_context():
        reset_data_table()
    response = client.get('/')
    assert b"Nil" in response.data
    assert b"No data yet" in response.data

