import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.models.customer import CustomerSchema
from src.models.schema.in_customer import InSetPasswordSchema

pytestmark = pytest.mark.asyncio


async def test_create_password_no_auth_forbidden_error(
    async_client: AsyncClient,
    set_password_input: InSetPasswordSchema,
    db_session: AsyncSession,
) -> None:
    response = await async_client.post(
        "/v1/customer/create-password", json=set_password_input.dict()
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Not authenticated"}


async def test_create_password_only_jwt_unauthorized_error(
    async_client_with_jwt: AsyncClient,
    set_password_input: InSetPasswordSchema,
    customer_factory: CustomerSchema,
    db_session: AsyncSession,
) -> None:
    db_session.add(customer_factory)
    await db_session.commit()
    response = await async_client_with_jwt.post(
        "/v1/customer/create-password", json=set_password_input.dict()
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Not authenticated"}


async def test_create_password_only_jwt_and_client_version(
    async_client_with_jwt_and_client_version: AsyncClient,
    set_password_input: InSetPasswordSchema,
    db_session: AsyncSession,
) -> None:
    response = await async_client_with_jwt_and_client_version.post(
        "/v1/customer/create-password", json=set_password_input.dict()
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"detail": "Not authenticated"}
