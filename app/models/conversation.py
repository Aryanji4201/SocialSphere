from datetime import datetime

from app.extensions import db


class Conversation(db.Model):

    __tablename__ = "conversations"

    id = db.Column(db.Integer, primary_key=True)

    participant_a = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    participant_b = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    messages = db.relationship(
    "Message",
    backref="conversation",
    lazy=True,
    cascade="all, delete-orphan"
)