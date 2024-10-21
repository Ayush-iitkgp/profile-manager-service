from fastapi import APIRouter, Depends
from starlette import status

from src.auth.jwt_token_auth import jwt_token_auth
from src.auth.verify_client import verify_client_version
from src.db.session import async_session
from src.models.schema.in_customer import (
    InChangePasswordSchema,
    InLoginSchema,
    InSetPasswordSchema,
)
from src.models.schema.out_customer import (
    OutDataChangePasswordSchema,
    OutDataLoginSchema,
    OutDataSetPasswordSchema,
)
from src.services.customer_service import CustomerService

router = APIRouter(dependencies=[Depends(verify_client_version)])


@router.post(
    "/create-password",
    status_code=status.HTTP_201_CREATED,
    response_model=OutDataSetPasswordSchema,
)
async def create_password(
    _: Depends(jwt_token_auth), password_data: InSetPasswordSchema
) -> OutDataSetPasswordSchema:
    async with async_session() as db:
        return await CustomerService.set_customer_password(db, password_data)


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=OutDataLoginSchema,
)
async def login(login_data: InLoginSchema) -> OutDataLoginSchema:
    async with async_session() as db:
        return await CustomerService.verify_customer_login(db, login_data)


@router.put(
    "/change-language",
    status_code=status.HTTP_200_OK,
    response_model=OutDataLoginSchema,
)
async def change_language(
    request_data: InChangePasswordSchema,
    _client_verified: None = Depends(verify_client_version),
) -> OutDataChangePasswordSchema:
    async with async_session() as db:
        return await CustomerService.change_customer_language(db, request_data)
