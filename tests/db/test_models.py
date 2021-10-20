from app.db import Data, Admin
from datetime import datetime
import random
import pytest


# TODO Change these to suites
def test_Admin_class(app):
    with app.test_request_context():
        assert Admin.verify_admin('test', 'test') == 1
        assert Admin.verify_admin('a', 'a') is None
        assert Admin.verify_admin('test', 'wrong') == "Incorrect password"

        test_Admin = Admin.add_admin('a', 'a')
        assert repr(test_Admin) == f'Admin(username="a", ' \
                                   f'password="{test_Admin.password}")'
        assert str(test_Admin) == '<Admin: a>'
        assert Admin.get_all_admin_usernames() == ['test', 'a']


def test_Data_class(app):
    with app.test_request_context():
        with pytest.raises(Exception) as e:
            Data.add_data("not a timestamp obj", 1, 2, 3, 4, 5, 6)
            assert e == "Not datetime object"
        timestamp = datetime.fromisoformat("2020-01-01 10:00:00")
        test_Data = Data.add_data(timestamp, 1, 1, 3, 2, 5, 3)
        assert repr(test_Data) == f'Data(timestamp={timestamp}, img1=1, img2=1, img3=3, img4=2, img5=5, highest=3)'
        assert str(test_Data) == f'<Data:{timestamp}, {test_Data.highest}>'
        assert str(Data.get_latest_entry()) == f'<Data:{timestamp}, {test_Data.highest}>'

        data_acc = []
        for _ in range(5):
            acc = []
            for _ in range(5):
                random_num = random.randint(0, 10)
                acc.append(random_num)
                t = timestamp.now()
            entry = Data(timestamp=t,
                         img1=acc[0],
                         img2=acc[1],
                         img3=acc[2],
                         img4=acc[3],
                         img5=acc[4],
                         highest=max(acc))
            Data.add_data_class(entry)

            data_acc.append(entry)

        data_acc.reverse()
        latest5 = Data.get_latest_n_entries(5)
        assert(latest5 == data_acc)
