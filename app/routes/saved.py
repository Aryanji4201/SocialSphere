from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.saved_post import SavedPost

saved = Blueprint("saved", __name__)


@saved.route("/saved-posts")
@login_required
def saved_posts():

    saved_posts = SavedPost.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "saved_posts.html",
        saved_posts=saved_posts
    )