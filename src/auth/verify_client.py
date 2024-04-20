from fastapi import Header
from packaging import version

from src import settings
from src.exceptions.core import HTTPForbiddenError


async def verify_client_version(client_version: str = Header(...)):
    required_version = version.parse(settings.REQUIRED_VERSION)
    current_version = version.parse(client_version)
    if current_version < required_version:
        raise HTTPForbiddenError
    return None
