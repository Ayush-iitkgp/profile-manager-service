import logging
from typing import Type
from uuid import UUID

from sqlalchemy import select

from src.db.errors import DoesNotExist
from src.db.repositories.base import BaseRepository
from src.db.tables.customer import Customer
from src.models.customer import CustomerSchema, InCustomerSchema

logger = logging.getLogger(__name__)


class CustomerRepository(BaseRepository):
    @property
    def _table(self) -> Type[Customer]:
        return Customer

    @property
    def _db_schema(self) -> Type[CustomerSchema]:
        return CustomerSchema

    @property
    def _in_create_schema(self) -> Type[InCustomerSchema]:
        return InCustomerSchema

    async def get_by_email(self, email: str) -> Type[CustomerSchema]:
        stmt = select(self._table).where(self._table.email == email)
        results = await self._db_session.execute(stmt)
        entry = results.scalars().first()
        if not entry:
            raise DoesNotExist(f"{self._table.__name__}<id:{email}> does not exist")
        return self._db_schema.from_orm(entry)

    async def get_by_customer_id(self, customer_id: UUID) -> Type[CustomerSchema]:
        stmt = select(self._table).where(self._table.customer_id == customer_id)
        results = await self._db_session.execute(stmt)
        entry = results.scalars().first()
        if not entry:
            raise DoesNotExist(
                f"{self._table.__name__}<id:{customer_id}> does not exist"
            )
        return self._db_schema.from_orm(entry)
