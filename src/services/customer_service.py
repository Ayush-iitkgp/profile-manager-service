import logging

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.errors import DoesNotExist
from src.db.repositories.customer import CustomerRepository
from src.exceptions.customer import (
    CustomerNotFoundError,
    CustomerPasswordNotUpdatedError,
)
from src.models.schema.in_customer import (
    InChangePasswordSchema,
    InLoginSchema,
    InSetPasswordSchema,
)
from src.models.schema.out_customer import (
    OutDataChangePasswordSchema,
    OutDataLoginSchema,
    OutDataSetPasswordSchema,
    OutLoginSchema,
    OutSetPasswordSchema,
)

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
            logger.info(f"Customer {customer.email} password created")
        except DoesNotExist:
            raise CustomerPasswordNotUpdatedError

        return OutDataSetPasswordSchema(
            data=OutSetPasswordSchema(
                message=f"Customer password has been set successfully for customer {password_data.email}."
            )
        )

    @classmethod
    async def verify_customer_login(
        cls,
        db: AsyncSession,
        password_data: InLoginSchema,
    ) -> OutDataLoginSchema:
        customer_repository = CustomerRepository(db_session=db)
        try:
            customer = await customer_repository.get_by_email(email=password_data.email)
        except DoesNotExist:
            raise CustomerNotFoundError
        # TODO: Implement the logic here
        # customer.set_password(password_data.password)
        # try:
        #     await customer_repository.update(customer.customer_id, customer.dict())
        #     logger.info(f"Customer {customer.email} password created")
        # except DoesNotExist:
        #     raise CustomerPasswordNotUpdatedError

        return OutDataLoginSchema(
            data=OutLoginSchema(
                customer_id=customer.customer_id, language=customer.language
            )
        )

    @classmethod
    async def change_customer_language(
        cls,
        db: AsyncSession,
        customer_id: InChangePasswordSchema,
    ) -> OutDataChangePasswordSchema:
        pass  # TODO: Implement the logic here
