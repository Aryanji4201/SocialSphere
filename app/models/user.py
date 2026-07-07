from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    bio = db.Column(db.Text)

    profile_picture = db.Column(db.String(255))

    private_account = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    location = db.Column(db.String(100))

    website = db.Column(db.String(255))

    cover_photo = db.Column(
        db.String(255),
        default="default_cover.jpg"
    )

    posts = db.relationship(
    "Post",
    backref="author",
    lazy=True,
    cascade="all, delete-orphan"
    )
    
    likes = db.relationship(
    "Like",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)
    followers = db.relationship(
    "Follow",
    foreign_keys="Follow.following_id",
    backref="following_user",
    lazy=True,
    cascade="all, delete-orphan"
)

    following = db.relationship(
        "Follow",
        foreign_keys="Follow.follower_id",
        backref="follower_user",
        lazy=True,
        cascade="all, delete-orphan"
)
    comments = db.relationship(
    "Comment",
    backref="author",
    lazy=True,
    cascade="all, delete-orphan"
)
    sent_notifications = db.relationship(
    "Notification",
    foreign_keys="Notification.sender_id",
    backref="sender",
    lazy=True,
    cascade="all, delete-orphan"
)

    received_notifications = db.relationship(
    "Notification",
    foreign_keys="Notification.receiver_id",
    backref="receiver",
    lazy=True,
    cascade="all, delete-orphan"
)
    conversations_started = db.relationship(
    "Conversation",
    foreign_keys="Conversation.participant_a",
    lazy=True
)

    conversations_received = db.relationship(
    "Conversation",
    foreign_keys="Conversation.participant_b",
    lazy=True
)
    messages = db.relationship(
    "Message",
    backref="sender",
    lazy=True,
    cascade="all, delete-orphan"
)
    saved_posts = db.relationship(
    "SavedPost",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)
    location = db.Column(
    db.String(100)
)

    website = db.Column(
        db.String(255)
    )

    cover_photo = db.Column(
        db.String(255),
        default="default_cover.jpg"
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    