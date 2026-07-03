from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.notification import Notification
from flask import jsonify
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

@notification.route("/api/notifications")
@login_required
def notifications_api():

    notifications = Notification.query.filter_by(
        receiver_id=current_user.id
    ).order_by(
        Notification.created_at.desc()
    ).limit(10).all()

    return jsonify([
        {
            "id": n.id,
            "message": n.message,
            "is_read": n.is_read,
            "time": n.created_at.strftime("%d %b %I:%M %p")
        }
        for n in notifications
    ])

@notification.route("/api/notifications/read", methods=["POST"])
@login_required
def mark_notifications_read():

    Notification.query.filter_by(
        receiver_id=current_user.id,
        is_read=False
    ).update({"is_read": True})

    db.session.commit()

    return jsonify({"success": True})
