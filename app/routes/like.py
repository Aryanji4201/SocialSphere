from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import jsonify
from flask_login import login_required
from flask_login import current_user

from app.extensions import db

from app.models.post import Post
from app.models.like import Like

from app.services.notification_service import create_notification

like = Blueprint("like", __name__)

@like.route("/like/<int:post_id>")
@login_required
def toggle_like(post_id):

    post = Post.query.get_or_404(post_id)

    existing_like = Like.query.filter_by(
        user_id=current_user.id,
        post_id=post.id
    ).first()

    if existing_like:

        db.session.delete(existing_like)
        liked = False

    else:

        new_like = Like(
            user_id=current_user.id,
            post_id=post.id
        )

        db.session.add(new_like)

        liked = True

        if post.author.id != current_user.id:
            create_notification(
                sender_id=current_user.id,
                receiver_id=post.author.id,
                notification_type="like",
                message=f"{current_user.username} liked your post.",
                post_id=post.id
            )

    db.session.commit()

    return jsonify({
        "liked": liked,
        "likes": len(post.likes)
    })