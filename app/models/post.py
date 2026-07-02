from datetime import datetime

from app.extensions import db


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    likes = db.relationship(
    "Like",
    backref="post",
    lazy=True,
    cascade="all, delete-orphan"
)
    comments = db.relationship(
    "Comment",
    backref="post",
    lazy=True,
    cascade="all, delete-orphan"
)
    notifications = db.relationship(
    "Notification",
    backref="post",
    lazy=True,
    cascade="all, delete-orphan"
)
    saved_by = db.relationship(
    "SavedPost",
    backref="post",
    lazy=True,
    cascade="all, delete-orphan"
)
    image = db.Column(
    db.String(255),
    nullable=True
)