from src.db.tables import Customer
from src.db.repositories.base import BaseRepository
from src.models.customer import CustomerSchema, InCustomerSchema
from typing import Type
import logging

logger = logging.getLogger(__name__)


class CustomerRepository(BaseRepository):
    @property
    def _table(self) -> Type[Currency]:
        return Currency

    @property
    def _db_schema(self) -> Type[CurrencySchema]:
        return CurrencySchema

    @property
    def _in_create_schema(self) -> Type[InCurrencySchema]:
        return InCurrencySchema