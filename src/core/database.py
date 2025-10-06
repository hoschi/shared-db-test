from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy import text
from src.core.config import settings
from src.core.middleware import schema_context


class SchemaAwareDatabase:
    """
    Manages schema-aware database connections using SQLAlchemy 2.0 and asyncpg.
    """

    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url, echo=False)
        self.session_factory = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Provide a transactional scope around a series of operations.
        Uses the schema from the context variable set by the middleware.
        """
        session = self.session_factory()
        schema = schema_context.get()
        try:
            if schema:
                # Use execute to set search_path.
                # NOTE: This is a simplified approach. For production, care should be taken
                # to prevent SQL injection if schema names come from untrusted sources.
                # In this project, schema names are controlled internally.
                await session.execute(text(f'SET search_path TO "{schema}"'))
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


db = SchemaAwareDatabase(settings.DATABASE_URL)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get a DB session.
    """
    async with db.get_session() as session:
        yield session