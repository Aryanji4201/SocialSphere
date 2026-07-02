from flask import Blueprint
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

    print("========== SAVE ==========")

    existing = SavedPost.query.filter_by(
        user_id=current_user.id,
        post_id=post_id
    ).first()

    print("Existing:", existing)

    if existing:

        print("Deleting...")

        db.session.delete(existing)

    else:

        print("Creating new save...")

        saved = SavedPost(
            user_id=current_user.id,
            post_id=post_id
        )

        db.session.add(saved)

    db.session.commit()

    print("Committed!")

    return redirect(url_for("home.dashboard"))