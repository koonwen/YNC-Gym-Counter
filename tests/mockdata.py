from app.db import db, Data, Admin
from datetime import datetime

def load_mock_data():
    # Data.mock_data(20)
    db.session.add(
        Data(timestamp=datetime.fromisoformat("2018-01-01 00:00:00"),
             img1=5, img2=6, img3=6, img4=3, img5=5, mode=5)
    )
    Admin.add_admin("test","test")
    db.session.commit()
    return