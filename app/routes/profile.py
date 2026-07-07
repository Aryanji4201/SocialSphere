
from flask import Blueprint, render_template
from flask_login import login_required
from app.models.user import User
import os
from flask import request
from flask import redirect
from flask import url_for
from flask_login import current_user
from app.extensions import db
from werkzeug.utils import secure_filename

from flask import current_app

profile = Blueprint("profile", __name__)

@profile.route("/profile/<int:user_id>")
@login_required

def user_profile(user_id):

    user = User.query.get_or_404(user_id)

    return render_template(
        "profile.html",
        profile=user
    )



@profile.route("/edit-profile", methods=["GET", "POST"])
@login_required
def edit_profile():

    if request.method == "POST":

        current_user.username = request.form["username"]
        current_user.bio = request.form["bio"]
        current_user.location = request.form["location"]
        current_user.website = request.form["website"]

        profile_picture = request.files.get("profile_picture")
        cover_photo = request.files.get("cover_photo")

        if profile_picture and profile_picture.filename:

            filename = secure_filename(profile_picture.filename)

            profile_picture.save(
                os.path.join(
                    current_app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            current_user.profile_picture = filename

        if cover_photo and cover_photo.filename:

            filename = secure_filename(cover_photo.filename)

            cover_photo.save(
                os.path.join(
                    current_app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            current_user.cover_photo = filename

        db.session.commit()

        return redirect(
            url_for(
                "profile.user_profile",
                user_id=current_user.id
            )
        )

    return render_template(
        "edit_profile.html"
    )