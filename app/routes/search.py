from flask import Blueprint
from flask import render_template
from flask import request

from flask_login import login_required

from app.models.user import User

search = Blueprint("search", __name__)

@search.route("/search")
@login_required
def search_users():

    query = request.args.get("q", "")

    users = []

    if query:

        users = User.query.filter(
            User.username.ilike(f"%{query}%")
        ).all()

    return render_template(
        "search.html",
        users=users,
        query=query
    )