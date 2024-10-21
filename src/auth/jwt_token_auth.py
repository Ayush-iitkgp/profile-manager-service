import logging
import uuid
from typing import Optional, Type

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from src import settings
from src.db.errors import DoesNotExist
from src.db.repositories.customer import CustomerRepository
from src.db.session import async_session
from src.exceptions.core import HTTPUnauthorizedError
from src.exceptions.customer import CustomerNotFoundError
from src.models.customer import CustomerSchema

logger = logging.getLogger(__name__)


class JWTBearer(HTTPBearer):
    def __init__(self):
        super().__init__(scheme_name="JWT Token")

    async def __call__(self, request: Request) -> Optional[Type[CustomerSchema]]:
        token: Optional[HTTPAuthorizationCredentials] = await super().__call__(
            request=request
        )
        if not token:
            return None

        try:
            payload = jwt.decode(
                token.credentials, settings.SECRET_KEY, algorithms=["HS256"]
            )
        except jwt.JWTError as e:
            raise HTTPUnauthorizedError() from e
        except Exception:
            return None

        customer_id = payload["customer_id"]

        customer = await self.get_customer_by_id(customer_id)

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token or user not found.",
            )
        return customer

    @staticmethod
    async def get_customer_by_id(customer_id: str) -> Type[CustomerSchema]:
        async with async_session() as db:
            try:
                customer = await CustomerRepository(db_session=db).get_by_customer_id(
                    customer_id=uuid.UUID(customer_id)
                )
                logger.info(
                    f"get_customer_by_id: Found customer with id: {customer_id}"
                )
            except DoesNotExist:
                raise CustomerNotFoundError
            return customer


jwt_token_auth = JWTBearer()
