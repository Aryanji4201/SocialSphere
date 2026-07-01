from flask import Blueprint
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from app.extensions import db

from app.models.user import User
from app.models.follow import Follow
from app.services.notification_service import create_notification

follow = Blueprint("follow", __name__)

@follow.route("/follow/<int:user_id>")
@login_required
def toggle_follow(user_id):

    if user_id == current_user.id:
        return redirect(url_for("profile.user_profile",
                                user_id=user_id))

    existing = Follow.query.filter_by(
        follower_id=current_user.id,
        following_id=user_id
    ).first()

    if existing:

        db.session.delete(existing)

    else:

        db.session.add(
            Follow(
                follower_id=current_user.id,
                following_id=user_id
            )
        )
        create_notification(
    sender_id=current_user.id,
    receiver_id=user_id,
    notification_type="follow",
    message=f"{current_user.username} started following you."
)

    db.session.commit()

    return redirect(
        url_for(
            "profile.user_profile",
            user_id=user_id
        )
    )