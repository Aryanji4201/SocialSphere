from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.post import Post
from app.models.follow import Follow
from app.models.user import User
print("Home blueprint loaded")
home = Blueprint("home", __name__)

@home.route("/")
@login_required
def dashboard():

    posts = Post.query.order_by(
        Post.created_at.desc()
    ).all()

    suggested_users = User.query.filter(
        User.id != current_user.id
    ).limit(5).all()

    return render_template(
        "dashboard.html",
        user=current_user,
        posts=posts,
        suggested_users=suggested_users
    )