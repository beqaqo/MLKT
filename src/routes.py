from flask import render_template, Blueprint, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user

from src.models import Lecture, Topic, User

main_bp = Blueprint('main', __name__)

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect("/admin")
        flash("User or password is incorrect")
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@main_bp.route('/')
def index():
    lectures = Lecture.query.all()

    return render_template('index.html', lectures=lectures)

@main_bp.route('/topic/<int:id>')
def topic(id):
    topic = Topic.query.get(id)

    return render_template('topic.html', topic=topic)