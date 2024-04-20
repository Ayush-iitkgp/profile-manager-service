import uuid
from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.base_class import Base
from src.db.session import async_session, engine
from src.models.customer import CustomerSchema
from src.models.schema.in_customer import InSetPasswordSchema


@pytest.fixture
def app() -> FastAPI:
    from src.app import app

    return app


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url="http://localhost:3000") as ac:
        yield ac


@pytest.fixture()
async def db_session() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        yield session
        await session.flush()
        await session.rollback()


@pytest.fixture()
async def customer_factory() -> CustomerSchema:
    customer = CustomerSchema(
        customer_id=uuid.UUID("06c2acac-7810-4dd8-8722-54bdb05fb9e4"),
        email="osefhhchnsic@protonmail.com",
        country="DE",
        language="de",
    )
    yield customer


@pytest.fixture()
async def set_password_input() -> InSetPasswordSchema:
    set_password_input = InSetPasswordSchema(
        email="osefhhchnsic@protonmail.com", password="1234", confirm_password="1234"
    )
    yield set_password_input
