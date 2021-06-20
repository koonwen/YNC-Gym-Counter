from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.TEXT, unique=True, nullable=False)
    password = db.Column(db.TEXT, unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class Data(db.Model):
    timestamp = db.Column(db.DATETIME, primary_key=True, default=datetime.utcnow)
    img1 = db.Column(db.Integer, nullable=False)
    img2 = db.Column(db.Integer, nullable=False)
    img3 = db.Column(db.Integer, nullable=False)
    img4 = db.Column(db.Integer, nullable=False)
    img5 = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<{self.timstamp}: {self.mode}>'