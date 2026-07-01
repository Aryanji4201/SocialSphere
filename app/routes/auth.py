from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_login import login_user
from flask_login import logout_user

from app.extensions import db
from app.models.user import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(
            username=username,
            email=email
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("register.html")



@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            login_user(user)

            return redirect(url_for("home.dashboard"))

    return render_template("login.html")



from flask_login import login_required

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))