from typing import Any, Dict, Optional

from fastapi import HTTPException
from starlette import status

from src import settings


class HTTPUnauthorizedError(HTTPException):
    def __init__(
        self,
        detail: str = "HTTP unauthorized error",
        headers: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers=headers
        )


class HTTPForbiddenError(HTTPException):
    def __init__(
        self,
        detail: str = f"Client version less than {settings.REQUIRED_VERSION} is not supported. "
        f"Please update your client.",
        headers: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN, detail=detail, headers=headers
        )


class HTTPUnprocessableEntityError(HTTPException):
    def __init__(
        self,
        detail: str = "Passwords do not match",
        headers: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
            headers=headers,
        )
