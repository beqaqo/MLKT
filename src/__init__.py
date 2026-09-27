from flask import Flask

from src.config import Config
from src.routes import main_bp, auth_bp
from src.ext import db, login_manager, admin
from src.commands import init_db, populate_db
from src.models import User, Lecture, Topic
from src.admin_views import LectureView, TopicView


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    #register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    #register extensions
    db.init_app(app)

    #register commands
    app.cli.add_command(init_db)
    app.cli.add_command(populate_db)

    #register flask_login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #register flask_admin
    admin.init_app(app)

    admin.add_view(LectureView(Lecture, db.session))
    admin.add_view(TopicView(Topic, db.session))

    return app