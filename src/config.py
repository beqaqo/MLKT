from os import path

class Config:
    BASE_DIR = path.dirname(path.abspath(__file__))
    UPLOAD_FOLDER = path.join(BASE_DIR, 'static/uploads')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite3')

    SECRET_KEY = 'this is really secret'