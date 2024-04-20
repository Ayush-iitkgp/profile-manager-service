class BaseDBError(Exception):
    pass


class DoesNotExist(BaseDBError):
    """Raised when record was not found in database."""
