from flask import Blueprint, request, redirect, url_for
from flask_login import login_required, current_user

from app.extensions import db
from app.models.comment import Comment
from app.models.post import Post

from app.services.notification_service import create_notification

comment = Blueprint("comment", __name__)

@comment.route("/comment/<int:post_id>", methods=["POST"])
@login_required
def add_comment(post_id):

    # Check if the post exists
    post = Post.query.get_or_404(post_id)

    content = request.form["content"].strip()

    # Prevent empty comments
    if not content:
        return redirect(url_for("home.dashboard"))

    new_comment = Comment(
        content=content,
        user_id=current_user.id,
        post_id=post.id
    )

    db.session.add(new_comment)

    create_notification(
    sender_id=current_user.id,
    receiver_id=post.author.id,
    notification_type="comment",
    message=f"{current_user.username} commented on your post.",
    post_id=post.id
)
    db.session.commit()

    return redirect(url_for("home.dashboard"))

@comment.route("/delete-comment/<int:comment_id>")
@login_required
def delete_comment(comment_id):

    comment = Comment.query.get_or_404(comment_id)

    # Allow only the author to delete
    if comment.user_id != current_user.id:
        return "Unauthorized", 403

    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for("home.dashboard"))