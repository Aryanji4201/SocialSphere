import os
import uuid

from flask import current_app

from app.extensions import db
from app.models.post import Post


class PostService:

    @staticmethod
    def create_post(content, image, user_id):

        filename = None

        if image and image.filename:

            extension = image.filename.rsplit(".", 1)[1].lower()

            filename = f"{uuid.uuid4()}.{extension}"

            image.save(
                os.path.join(
                    current_app.config["UPLOAD_FOLDER"],
                    filename
                )
            )

        post = Post(
            content=content,
            image=filename,
            user_id=user_id
        )

        db.session.add(post)
        db.session.commit()

        return post