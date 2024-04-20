import logging
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src import settings
logger = logging.getLogger(__name__)


engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=settings.DATABASE_POOL_SIZE,
    pool_pre_ping=True,
    echo=True,
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    pass