from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import Blueprint, jsonify
from flask import redirect
from flask import url_for
from flask_login import login_required
from flask_login import current_user

from app.extensions import db
from app.models.saved_post import SavedPost

save = Blueprint("save", __name__)
@save.route("/save/<int:post_id>")
@login_required
def save_post(post_id):

    existing = SavedPost.query.filter_by(
        user_id=current_user.id,
        post_id=post_id
    ).first()

    if existing:

        db.session.delete(existing)
        saved = False

    else:

        new_save = SavedPost(
            user_id=current_user.id,
            post_id=post_id
        )

        db.session.add(new_save)
        saved = True

    db.session.commit()

    total_saves = SavedPost.query.filter_by(post_id=post_id).count()

    return jsonify({
        "saved": saved,
        "count": total_saves
    })