import pytest
from httpx import AsyncClient
from starlette import status

from src.models.schema.in_customer import InSetPasswordSchema

pytestmark = pytest.mark.asyncio


async def test_create_password_no_auth(
    async_client: AsyncClient, set_password_input: InSetPasswordSchema
) -> None:
    response = await async_client.post(
        "/v1/customer/create-password", data=set_password_input
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Not authenticated"}
