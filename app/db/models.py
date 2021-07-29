from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import random

db = SQLAlchemy()


class Admin(db.Model):
    """Admin user class"""
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.TEXT, unique=True, nullable=False)
    password = db.Column(db.TEXT, unique=True, nullable=False)

    def __repr__(self):
        return f'Admin(username="{self.username}", password="{self.password}")'

    def __str__(self):
        return f'<Admin: {self.username}>'

    @staticmethod
    def add_admin(username, password):
        new_admin = Admin(username=username, password=generate_password_hash(password))
        db.session.add(new_admin)
        db.session.commit()
        return new_admin

    @classmethod
    def verify(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user is None:
            return
        if check_password_hash(user.password, password):
            return user._id
        return "Incorrect password"


class Data(db.Model):
    """Database entries"""
    timestamp = db.Column(db.DATETIME, primary_key=True, default=datetime.utcnow)
    img1 = db.Column(db.Integer, nullable=False)
    img2 = db.Column(db.Integer, nullable=False)
    img3 = db.Column(db.Integer, nullable=False)
    img4 = db.Column(db.Integer, nullable=False)
    img5 = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Data(timestamp={self.timestamp}, ' \
               f'img1={self.img1}, ' \
               f'img2={self.img2}, ' \
               f'img3={self.img3}, ' \
               f'img4={self.img4}, ' \
               f'img5={self.img5}, ' \
               f'mode={self.mode})'

    def __str__(self):
        return f'<Data:{self.timestamp}, {self.mode}>'

    #TODO add validation
    @staticmethod
    def add_data(timestamp, img1, img2, img3, img4, img5, mode):
        if not isinstance(timestamp, datetime):
            raise Exception("Not datetime object")
        new_data = Data(timestamp=timestamp,
                        img1=img1,
                        img2=img2,
                        img3=img3,
                        img4=img4,
                        img5=img5,
                        mode=mode)
        db.session.add(new_data)
        db.session.commit()
        return new_data

    @staticmethod
    def get_latest():
        """Return latest entry in the table"""
        return Data.query.order_by(Data.timestamp.desc()).first()

    @classmethod
    def get_latest_mode(cls):
        """return just the mode of the latest entry, returns None if N/A"""
        entry = cls.get_latest()
        return entry.mode

    @staticmethod
    def mock_data(entries=1):
        """Generate specified number of random data entries """
        for i in range(entries):
            lst = [random.randint(0, 10) for j in range(5)]
            lst.sort()
            db.session.add(Data(timestamp=datetime.now(),
                                img1=lst[0],
                                img2=lst[1],
                                img3=lst[2],
                                img4=lst[3],
                                img5=lst[4],
                                mode=lst[2]))
        return
