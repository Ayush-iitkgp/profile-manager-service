from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from your_database_module import get_db, User  # Import your SQLAlchemy models and database session here


class BearerTokenAuth(HTTPBearer):
    def __init__(self):
        super().__init__()

    async def __call__(self, credentials: HTTPAuthorizationCredentials = Depends()):
        if credentials.scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authentication scheme. Use Bearer token.",
            )

        if not credentials.credentials:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Bearer token is missing.",
            )

        token = credentials.credentials
        user = self.get_user_by_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token or user not found.",
            )

        return user

    def get_user_by_token(self, token: str):
        # Implement logic to fetch user by token from the database
        # Assuming you have a User model with a field customer_id
        # Also, assuming you have a function `get_db` to get the database session
        db: Session = get_db()
        user = db.query(User).filter(User.token == token).first()
        if not user:
            return None
        return user if user.customer_id else None


bearer_auth = BearerTokenAuth()
