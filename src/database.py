from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from src.config import settings


engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True
)

session_factory = sessionmaker(engine)
async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
