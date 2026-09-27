from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.ext import db

class BaseModel(db.Model):
    __abstract__ = True

    deleted = db.Column(db.Boolean, default=False)

    def create(self, save=True):
        db.session.add(self)

        if save:
            self.save()

    def save(self):
        db.session.commit()

    def delete(self, save=True):
        self.deleted = True

        if save:
            self.save()

class User(BaseModel, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    _password = db.Column(db.String)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.email}'

class Lecture(BaseModel):
    __tablename__ = 'lecture'

    id = db.Column(db.Integer, primary_key=True)

    icon = db.Column(db.String)
    color = db.Column(db.String)
    title = db.Column(db.String(100), nullable=False)
    week = db.Column(db.Integer)

    topics = db.relationship('Topic', back_populates='lecture')

    def __repr__(self):
        return f'{self.title[0:15]} - week {self.week}'

class Topic(BaseModel):
    __tablename__ = 'topic'

    id = db.Column(db.Integer, primary_key=True)

    icon = db.Column(db.String)
    title = db.Column(db.String)
    google_colab_link = db.Column(db.String)

    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    lecture = db.relationship('Lecture', back_populates='topics')

    def __repr__(self):
        return f'{self.title[0:15]}'