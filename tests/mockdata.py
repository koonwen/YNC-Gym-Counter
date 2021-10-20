from app.db import db, Data, Admin
from datetime import datetime

def load_mock_data():
    # Data.mock_data(20)
    db.session.add(
        Data(timestamp=datetime.fromisoformat("2018-01-01 00:00:00"),
             img1=5, img2=3, img3=2, img4=2, img5=1, highest=5)
    )
    db.session.add(
        Data(timestamp=datetime.fromisoformat("2018-01-01 00:20:00"),
             img1=5, img2=6, img3=6, img4=3, img5=5, highest=6)
    )
    db.session.add(
        Data(timestamp=datetime.fromisoformat("2020-01-01 00:50:00"),
             img1=1, img2=1, img3=1, img4=3, img5=4, highest=4)
    )
    db.session.add(
        Data(timestamp=datetime.fromisoformat("2018-01-01 00:51:00"),
             img1=2, img2=1, img3=1, img4=2, img5=1, highest=2)
    )
    db.session.add(
        Data(timestamp=datetime.fromisoformat("2018-01-01 00:52:00"),
             img1=1, img2=1, img3=0, img4=0, img5=0, highest=1)
    )
    Admin.add_admin("test","test")
    db.session.commit()
    return