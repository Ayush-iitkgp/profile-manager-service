from fastapi import HTTPException
from starlette import status


class BaseError(HTTPException):
    pass


class CustomerError(BaseError):
    pass


class CustomerNotFoundError(CustomerError):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer Not Found"
        )


class CustomerIncorrectUsernameOrPasswordError(CustomerError):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password",
        )


class CustomerPasswordIncorrectError(CustomerError):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )


class CustomerPasswordNotUpdatedError(CustomerError):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Customer password could not be updated",
        )
