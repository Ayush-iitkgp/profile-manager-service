import logging
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repositories.customer import CustomerRepository
from src.models.schema.out_customer import OutDataSetPasswordSchema, OutSetPasswordSchema
from src.models.schema.in_customer import InSetPasswordSchema
from src.db.errors import DoesNotExist
from src.exceptions.customer import CustomerNotFoundError, CustomerPasswordNotUpdatedError
logger = logging.getLogger(__name__)


class CustomerService:

    @classmethod
    async def set_customer_password(
            cls,
            db: AsyncSession,
            password_data: InSetPasswordSchema,
    ) -> OutDataSetPasswordSchema:
        customer_repository = CustomerRepository(db_session=db)
        try:
            customer = await customer_repository.get_by_email(email=password_data.email)
        except DoesNotExist:
            raise CustomerNotFoundError
        customer.set_password(password_data.password)
        try:
            await customer_repository.update(customer.customer_id, customer.dict())
        except DoesNotExist:
            raise CustomerPasswordNotUpdatedError

        return OutDataSetPasswordSchema(
            data=OutSetPasswordSchema(message="Customer password has been set successfully."))

    @classmethod
    async def delete_customer_by_currency_id(
            cls,
            db: AsyncSession,
            customer_id: UUID,
    ) -> None:
        customer_repository = CustomerRepository(db_session=db)
        try:
            currency = await customer_repository.get_by_id(entry_id=customer_id)
        except DoesNotExist:
            raise CustomerNotFoundError

        # try:
        #     await customer_repository.delete_cus_by_currency_id(currency_id=currency.id)
        #     await db.commit()
        # except Exception:
        #     await db.rollback()
        #     raise CustomerPasswordNotUpdatedError