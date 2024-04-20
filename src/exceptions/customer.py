from fastapi import HTTPException
from starlette import status
from typing import Dict, Optional, Any


class BaseError(HTTPException):
    pass


class CustomerError(BaseError):
    pass


class CustomerNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")


class CustomerPasswordNotUpdatedError(CustomerError):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Customer password could not be updated")


class HTTPUnauthorizedError(HTTPException):
    def __init__(
        self,
        detail: str = "HTTP unauthorized error",
        headers: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail, headers=headers)


class HTTPUnprocessableEntityError(HTTPException):
    def __init__(
        self,
        detail: str = "Passwords do not match",
        headers: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail, headers=headers)