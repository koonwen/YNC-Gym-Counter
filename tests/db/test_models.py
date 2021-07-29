from app.db import Data, Admin
from datetime import datetime
import pytest


def test_Admin_class(app):
    with app.test_request_context():
        assert Admin.verify('test', 'test') == 1
        assert Admin.verify('a', 'a') is None
        assert Admin.verify('test', 'wrong') == "Incorrect password"

        test_Admin = Admin.add_admin('a', 'a')
        assert repr(test_Admin) == f'Admin(username="a", ' \
                                   f'password="{test_Admin.password}")'
        assert str(test_Admin) == '<Admin: a>'


def test_Data_class(app):
    with app.test_request_context():
        with pytest.raises(Exception) as e:
            Data.add_data("not a timestamp obj", 1, 2, 3, 4, 5, 6)
            assert e == "Not datetime object"
        timestamp = datetime.fromisoformat("2020-01-01 00:00:00")
        test_Data = Data.add_data(timestamp, 1, 1, 3, 2, 5, 3)
        assert repr(test_Data) == f'Data(timestamp={timestamp}, img1=1, img2=1, img3=3, img4=2, img5=5, mode=3)'
        assert str(test_Data) == f'<Data:{timestamp}, {test_Data.mode}>'

        assert str(Data.get_latest()) == f'<Data:{timestamp}, {test_Data.mode}>'
        assert Data.get_latest_mode() == test_Data.mode
