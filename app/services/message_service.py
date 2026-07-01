from app.models.follow import Follow


def can_message(user1_id, user2_id):
    """
    Return True only if both users follow each other.
    """

    follows_1 = Follow.query.filter_by(
        follower_id=user1_id,
        following_id=user2_id
    ).first()

    follows_2 = Follow.query.filter_by(
        follower_id=user2_id,
        following_id=user1_id
    ).first()

    return follows_1 is not None and follows_2 is not None