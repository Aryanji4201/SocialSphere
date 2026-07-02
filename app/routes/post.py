import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app
from app.services.post_service import PostService
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from app.extensions import db
from app.models.post import Post

from flask import render_template

post = Blueprint("post", __name__)

@post.route("/create-post", methods=["POST"])
@login_required
def create_post():

    content = request.form["content"].strip()

    if not content:
        return redirect(url_for("home.dashboard"))

    image = request.files.get("image")

    PostService.create_post(
        content=content,
        image=image,
        user_id=current_user.id
    )

    return redirect(url_for("home.dashboard"))

@post.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):

    post_obj = Post.query.get_or_404(post_id)

    if post_obj.user_id != current_user.id:
        return "Unauthorized", 403

    if request.method == "POST":

        post_obj.content = request.form["content"]

        db.session.commit()

        return redirect(url_for("home.dashboard"))

    return render_template(
        "edit_post.html",
        post=post_obj
    )

@post.route("/delete-post/<int:post_id>")
@login_required
def delete_post(post_id):

    post_obj = Post.query.get_or_404(post_id)

    db.session.delete(post_obj)

    db.session.commit()

    return redirect(url_for("home.dashboard"))
