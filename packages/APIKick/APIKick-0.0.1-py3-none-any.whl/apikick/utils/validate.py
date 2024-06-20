import uuid


def validate_username(username: str):
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    return True


def validate_video_id(video_uuid: str):
    try:
        val = uuid.UUID(video_uuid, version=4)
    except ValueError:
        raise ValueError("Invalid UUID format.")
    if str(val) != video_uuid:
        raise ValueError("Invalid UUID format.")
    return True
