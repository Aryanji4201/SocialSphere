from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify
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
@search.route("/api/search")
@login_required
def live_search():

    query = request.args.get("q", "").strip()

    if len(query) < 1:
        return jsonify([])

    users = User.query.filter(
        User.username.ilike(f"%{query}%")
    ).limit(6).all()

    results = []

    for user in users:

        results.append({
            "id": user.id,
            "username": user.username,
            "avatar": f"https://ui-avatars.com/api/?name={user.username}"
        })

    return jsonify(results)