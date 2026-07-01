from app.extensions import db
from app.models.notification import Notification


def create_notification(
    sender_id,
    receiver_id,
    notification_type,
    message,
    post_id=None
):
    # Don't notify yourself
    if sender_id == receiver_id:
        return

    notification = Notification(
        sender_id=sender_id,
        receiver_id=receiver_id,
        type=notification_type,
        message=message,
        post_id=post_id
    )

    db.session.add(notification)