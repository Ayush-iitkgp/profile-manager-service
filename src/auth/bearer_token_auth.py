import uuid

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.db.errors import DoesNotExist
from src.db.repositories.customer import CustomerRepository
from src.db.session import async_session


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

        customer_id = credentials.credentials
        customer = self.get_customer_by_id(customer_id)
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token or user not found.",
            )
        return customer

    async def get_customer_by_id(self, customer_id: str):
        async with async_session():
            try:
                customer = CustomerRepository.get_by_customer_id(uuid.UUID(customer_id))
            except DoesNotExist:
                return None
            return customer


bearer_auth = BearerTokenAuth()
