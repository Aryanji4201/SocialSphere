
from flask import Blueprint, render_template
from flask_login import login_required
from app.models.user import User

profile = Blueprint("profile", __name__)

@profile.route("/profile/<int:user_id>")
@login_required

def user_profile(user_id):

    user = User.query.get_or_404(user_id)

    return render_template(
        "profile.html",
        profile=user
    )

from flask import request
from flask import redirect
from flask import url_for
from flask_login import current_user
from app.extensions import db
@profile.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.bio = request.form["bio"]

        db.session.commit()

        return redirect(
            url_for(
                "profile.user_profile",
                user_id=current_user.id
            )
        )

    return render_template("edit_profile.html")
