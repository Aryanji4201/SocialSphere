import os

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://aryan:Aryan%40123@localhost/social_media"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "app/static/uploads"

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB
