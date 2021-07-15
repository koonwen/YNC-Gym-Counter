from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import random
from flask import current_app

db = SQLAlchemy()


class Admin(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.TEXT, unique=True, nullable=False)
    password = db.Column(db.TEXT, unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def verify(self, username, password):
        user = Admin.query.filter_by(username=username)
        if user is None:
            return
        if check_password_hash(user.password, password):
            return user._id

    @staticmethod
    def add_admin(username, password):
        db.session.add(Admin(username=username, password=password))
        db.session.commit()

class Data(db.Model):
    timestamp = db.Column(db.DATETIME, primary_key=True, default=datetime.utcnow)
    img1 = db.Column(db.Integer, nullable=False)
    img2 = db.Column(db.Integer, nullable=False)
    img3 = db.Column(db.Integer, nullable=False)
    img4 = db.Column(db.Integer, nullable=False)
    img5 = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<{self.timestamp}: {self.mode}>'

    @staticmethod
    def mock_data(rows=1):
        for i in range(rows):
            l = [random.randint(0,10) for j in range(5)]
            l.sort()
            db.session.add(Data(timestamp=datetime.now(),
                                img1=l[0],
                                img2=l[1],
                                img3=l[2],
                                img4=l[3],
                                img5=l[4],
                                mode=l[2]))
        return db.session.commit()
