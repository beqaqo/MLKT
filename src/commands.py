import click
from flask.cli import with_appcontext

from src.models import Lecture, Topic, User
from src.ext import db

@click.command('init_db')
@with_appcontext
def init_db():
    print('Initializing database...')
    db.drop_all()
    db.create_all()
    print('Database initialized.')

@click.command('populate_db')
@with_appcontext
def populate_db():
    print('Populating database...')

    Lecture(title='Introduction to Machine Learning', week=1).create()
    Lecture(title='Model Evaluation and Model Selection', week=2).create()
    Lecture(title='Linear Models', week=3).create()
    Lecture(title='Probabilistic Models', week=4).create()

    Topic(title='Exploratory Data Analisys', lecture_id=1).create(save=False)
    Topic(title='Types Of Machine Learning', lecture_id=1).create(save=False)
    Topic(title='ML Workflow', lecture_id=1).create(save=False)

    Topic(title='Data Splitting and Cross Validation', lecture_id=2).create(save=False)
    Topic(title='Regularisation', lecture_id=2).create(save=False)

    Topic(title='System of Linear Equations', lecture_id=3).create(save=False)
    Topic(title='Loss Funqtion', lecture_id=3).create(save=False)
    Topic(title='Gradient Descent', lecture_id=3).create(save=False)

    Topic(title='Probability Distributions', lecture_id=4).create()

    User(email='admin@gmail.com', password='password123').create()

    print('Database populated.')




