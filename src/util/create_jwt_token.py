import uuid
from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from src import settings


async def create_access_token(
    customer_id: uuid, expires_delta: Optional[timedelta] = None
):
    """
    :param customer_id: we only use customer_id for the jwt token encodind # TODO: Research why can't I used email,
    customer_id and language for the jwt token generation
    :param expires_delta: by default our JWT token will be valid for 15 minutes
    :return:
    """
    to_encode = {"customer_id": customer_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm="HS256"
    )  # TODO: Research which is the best algorithm from encoding jwt key
    return encoded_jwt
