from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.notification import Notification

notification = Blueprint("notification", __name__)

@notification.route("/notifications")
@login_required
def notifications():

    notifications = Notification.query.filter_by(
        receiver_id=current_user.id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return render_template(
        "notifications.html",
        notifications=notifications
    )