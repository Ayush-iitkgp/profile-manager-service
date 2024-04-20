# import uuid

from fastapi import APIRouter

# Depends
from starlette import status

# from src.models.schema.out_pnl import OutDataPnlSchema
# from src.db.session import async_session
# from src.services.pnl_service import PnlService
# from src.auth.basic_authorization import basic_auth

router = APIRouter()


# @router.get(
#     "/{currencyId}/", status_code=status.HTTP_200_OK, response_model=OutDataPnlSchema
# )
# async def get_pnl_for_currency(
#         currencyId: uuid.UUID,
#         _: str = Depends(basic_auth),
# ) -> OutDataPnlSchema:
#     async with async_session() as db:
#         return await PnlService.get_pnl_by_currency_id(db, currencyId)


@router.get("/", status_code=status.HTTP_200_OK)
async def customer_router():
    return "customer router working"
