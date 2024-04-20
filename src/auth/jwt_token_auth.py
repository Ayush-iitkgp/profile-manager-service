import logging
import uuid
from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from src import settings
from src.exceptions.core import HTTPForbiddenError, HTTPUnauthorizedError
from src.exceptions.customer import CustomerNotFoundError
from src.models.customer import CustomerSchema

logger = logging.getLogger(__name__)


class JWTBearer(HTTPBearer):
    def __init__(self):
        super().__init__(
            scheme_name="Firebase ID Token",
            auto_error=False,
        )

    async def __call__(self, request: Request) -> Optional[CustomerSchema]:
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

        # TODO: Improve this code
        # customer_id = payload['customer_id']

        # customer = await self.get_customer_by_id(customer_id)
        #
        # if not customer:
        #     raise HTTPException(
        #         status_code=status.HTTP_403_FORBIDDEN,
        #         detail="Invalid token or user not found.",
        #     )
        # return customer

    # async def get_customer_by_id(self, customer_id: str):
    #     async with async_session():
    #         try:
    #             customer = CustomerRepository.get_by_customer_id(
    #                 customer_id=uuid.UUID(customer_id)
    #             )
    #             logger.info(f"Found customer with id: {customer_id}")
    #         except DoesNotExist:
    #             raise CustomerNotFoundError
    #         return customer


jwt_token_auth = JWTBearer()
