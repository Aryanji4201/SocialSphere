from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.post import Post
from app.models.follow import Follow

print("Home blueprint loaded")
home = Blueprint("home", __name__)

@home.route("/")
@login_required
def dashboard():

    # posts = Post.query.order_by(
    #     Post.created_at.desc()
    # ).all()
    following = Follow.query.filter_by(
    follower_id=current_user.id
    ).all()

    following_ids = [
    follow.following_id
    for follow in following
]
    following_ids.append(current_user.id)

    posts = Post.query.filter(
    Post.user_id.in_(following_ids)
).order_by(
    Post.created_at.desc()
).all()


    return render_template(

        "dashboard.html",

        user=current_user,

        posts=posts

    )

