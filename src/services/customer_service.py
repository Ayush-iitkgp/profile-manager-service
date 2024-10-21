import logging

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.errors import DoesNotExist
from src.db.repositories.customer import CustomerRepository
from src.exceptions.customer import (
    CustomerIncorrectUsernameOrPasswordError,
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
            logger.info(
                f"set_customer_password: Customer found with email: {password_data.email}"
            )
        except DoesNotExist:
            logger.error(
                f"set_customer_password: Customer not found with email: {password_data.email}"
            )
            raise CustomerNotFoundError
        customer.set_hashed_password(password_data.password)
        try:
            await customer_repository.update(customer.customer_id, customer.dict())
            logger.info(f"Customer {customer.email} password created")
        except DoesNotExist:
            raise CustomerPasswordNotUpdatedError

        await db.commit()
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
        except DoesNotExist as e:
            raise CustomerIncorrectUsernameOrPasswordError() from e
        if customer.is_password_correct(password_data.password):
            return OutDataLoginSchema(
                data=OutLoginSchema(
                    customer_id=str(customer.customer_id), language=customer.language
                )
            )
        else:
            raise CustomerIncorrectUsernameOrPasswordError()

    @classmethod
    async def change_customer_language(
        cls,
        db: AsyncSession,
        customer_id: InChangePasswordSchema,
    ) -> OutDataChangePasswordSchema:
        pass  # TODO: Implement the logic here
