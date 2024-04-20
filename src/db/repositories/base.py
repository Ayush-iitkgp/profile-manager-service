import abc
import uuid
from typing import List, Type, TypeVar, Union
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.errors import DoesNotExist
from src.models.base_model import BaseSchema

TABLE = TypeVar("TABLE")
SCHEMA = TypeVar("SCHEMA", bound=BaseSchema)
IN_SCHEMA = TypeVar("IN_SCHEMA", bound=BaseSchema)


class BaseRepository(metaclass=abc.ABCMeta):
    """
    Abstract class for use in all tables.
    """

    def __init__(self, db_session: AsyncSession, *args, **kwargs) -> None:
        self._db_session: AsyncSession = db_session

    @property
    @abc.abstractmethod
    def _table(self) -> Type[TABLE]:
        pass

    @property
    @abc.abstractmethod
    def _in_create_schema(self) -> Type[IN_SCHEMA]:
        pass

    @property
    @abc.abstractmethod
    def _db_schema(self) -> Type[SCHEMA]:
        pass

    def _preprocess_create(self, values: dict) -> dict:
        values["id"] = uuid.uuid4()

        return values

    async def create(self, values: Union[SCHEMA, dict], commit: bool = True) -> SCHEMA:
        if isinstance(values, dict):
            values = self._in_create_schema(**values)
        dict_values = values.dict()

        entry = self._table(**dict_values)
        self._db_session.add(entry)
        if commit:
            await self._db_session.commit()

        return self._db_schema.from_orm(entry)

    async def get_by_id(self, entry_id: UUID) -> SCHEMA:
        entry = await self._db_session.get(self._table, entry_id)
        if not entry:
            raise DoesNotExist(f"{self._table.__name__}<id:{entry_id}> does not exist")
        return self._db_schema.from_orm(entry)

    async def list(self) -> List[SCHEMA]:
        stmt = select(self._table)
        results = await self._db_session.execute(stmt)
        entries = results.scalars().all()
        if not entries:
            return []
        return [self._db_schema.from_orm(entry) for entry in entries]

    async def update(self, entry_id: UUID, values: Union[SCHEMA, dict]) -> SCHEMA:
        stmt = (
            update(self._table)
            .where(self._table.id == entry_id)
            .values(**dict(values))
            .returning(*self._table.__table__.columns)
        )
        orm_stmt = (
            select(self._table)
            .from_statement(stmt)
            .execution_options(populate_existing=True)
        )
        results = await self._db_session.execute(orm_stmt)
        entry = results.first()
        if not entry:
            raise DoesNotExist(f"{self._table.__name__}<id:{entry_id}> does not exist")
        return self._db_schema.from_orm(entry[0])
