from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    writings = db.relationship('Writing', backref = 'user', lazy=True)

    def __repr__(self):
        return '<User: [{}]>'.format(self.email)


class Writing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    title = db.Column(db.String(100))
    prompt = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Writing: [{}]|by [{}]>'.format(self.title, self.user)


