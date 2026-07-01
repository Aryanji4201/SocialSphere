from flask import Blueprint
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from app.extensions import db

from app.models.conversation import Conversation
from app.models.user import User

from app.services.message_service import can_message

from flask import request
from flask import render_template

from app.models.message import Message

message = Blueprint("message", __name__)

@message.route("/messages")
@login_required
def conversations():

    conversations = Conversation.query.filter(
        (Conversation.participant_a == current_user.id) |
        (Conversation.participant_b == current_user.id)
    ).order_by(
        Conversation.created_at.desc()
    ).all()

    conversation_data = []

    for conversation in conversations:

        if conversation.participant_a == current_user.id:
            other_user = User.query.get(conversation.participant_b)
        else:
            other_user = User.query.get(conversation.participant_a)

        last_message = Message.query.filter_by(
            conversation_id=conversation.id
        ).order_by(
            Message.created_at.desc()
        ).first()

        conversation_data.append({
            "conversation": conversation,
            "other_user": other_user,
            "last_message": last_message
        })

    return render_template(
        "conversations.html",
        conversations=conversation_data
    )

@message.route("/message/<int:user_id>")
@login_required
def start_chat(user_id):

    if user_id == current_user.id:
        return redirect(url_for("profile.view_profile",
                                user_id=current_user.id))

    user = User.query.get_or_404(user_id)

    if not can_message(current_user.id, user.id):
        return "You can only message mutual followers.", 403

    conversation = Conversation.query.filter(

        (
            (Conversation.participant_a == current_user.id) &
            (Conversation.participant_b == user.id)

        ) |

        (
            (Conversation.participant_a == user.id) &
            (Conversation.participant_b == current_user.id)
        )

    ).first()

    if conversation is None:

        conversation = Conversation(

            participant_a=current_user.id,

            participant_b=user.id

        )

        db.session.add(conversation)

        db.session.commit()

    return redirect(
        url_for(
            "message.chat",
            conversation_id=conversation.id
        )
    )

@message.route("/chat/<int:conversation_id>", methods=["GET", "POST"])
@login_required
def chat(conversation_id):

    conversation = Conversation.query.get_or_404(conversation_id)

    # Security check
    if current_user.id not in [
        conversation.participant_a,
        conversation.participant_b
    ]:
        return "Unauthorized", 403

    if request.method == "POST":

        content = request.form["content"].strip()

        if content:

            new_message = Message(
                conversation_id=conversation.id,
                sender_id=current_user.id,
                content=content
            )

            db.session.add(new_message)
            db.session.commit()

            return redirect(
                url_for(
                    "message.chat",
                    conversation_id=conversation.id
                )
            )

    messages = Message.query.filter_by(
        conversation_id=conversation.id
    ).order_by(
        Message.created_at.asc()
    ).all()

    # Find the other user
    if current_user.id == conversation.participant_a:
        other_user = User.query.get(conversation.participant_b)
    else:
        other_user = User.query.get(conversation.participant_a)

    return render_template(
        "chat.html",
        conversation=conversation,
        messages=messages,
        other_user=other_user
    )