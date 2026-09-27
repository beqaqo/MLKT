from flask_admin.contrib.sqla import ModelView
from flask_admin.model import InlineFormAdmin
from flask_admin.form import ImageUploadField
from flask_login import current_user
from flask import redirect, url_for
from markupsafe import Markup
from uuid import uuid4
import os

from src.config import Config
from src.models import Topic

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))


class TopicInline(InlineFormAdmin):
    form_overrides = {
        "icon": ImageUploadField
    }

    form_args = {
        "icon": {
            "base_path": lambda: Config.UPLOAD_FOLDER,
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }

    column_formatters = {'icon': lambda s, c, m, n: Markup(f'<img src="/static/{m.icon}" width="100">') }

class LectureView(SecureModelView):
    create_modal = True
    edit_modal = True

    form_overrides = {
        "icon": ImageUploadField
    }

    form_args = {
        "icon": {
            "base_path": lambda: Config.UPLOAD_FOLDER,
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }

    column_formatters = {'icon': lambda s, c, m, n: Markup(f'<img src="/static/{m.icon}" width="100">') }

    inline_models = [TopicInline(Topic)]


class TopicView(SecureModelView):
    create_modal = True
    edit_modal = True

    form_overrides = {
        "icon": ImageUploadField
    }

    form_args = {
        "icon": {
            "base_path": lambda: Config.UPLOAD_FOLDER,
            "relative_path": "images/",
            "namegen": lambda obj, file: f"{uuid4().hex}{os.path.splitext(file.filename)[1]}"
        }
    }

    column_formatters = {'icon': lambda s, c, m, n: Markup(f'<img src="/static/{m.icon}" width="100">') }
