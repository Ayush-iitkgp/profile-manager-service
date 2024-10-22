import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.schema.in_customer import InSetPasswordSchema
from src.models.schema.out_customer import (
    OutDataSetPasswordSchema,
    OutSetPasswordSchema,
)
from src.services.customer_service import CustomerService

pytestmark = pytest.mark.asyncio


@pytest.mark.xfail
async def test_set_customer_password(
    db_session: AsyncSession, set_password_input: InSetPasswordSchema
) -> None:
    response = await CustomerService.set_customer_password(
        db=db_session, password_data=set_password_input
    )
    assert response == OutDataSetPasswordSchema(
        data=OutSetPasswordSchema(
            message=f"Customer {set_password_input.email} password created"
        )
    )
