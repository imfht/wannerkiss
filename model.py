import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    ip = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.title
