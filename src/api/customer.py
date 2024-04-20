from fastapi import APIRouter, Depends
from starlette import status

from src.auth.bearer_token_auth import bearer_auth
from src.db.session import async_session
from src.models.schema.in_customer import InSetPasswordSchema
from src.models.schema.out_customer import OutDataSetPasswordSchema
from src.services.customer_service import CustomerService

router = APIRouter()


@router.post(
    "/create-password/",
    status_code=status.HTTP_200_OK,
    response_model=OutDataSetPasswordSchema,
)
async def create_password(
    password_data: InSetPasswordSchema,
    _: str = Depends(bearer_auth),
) -> OutDataSetPasswordSchema:
    async with async_session() as db:
        return await CustomerService.set_customer_password(db, password_data)
