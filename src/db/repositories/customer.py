import logging
from typing import Type

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
