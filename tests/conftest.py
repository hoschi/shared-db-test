import asyncio
from typing import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import SchemaAwareDatabase, db
from src.core.middleware import SchemaRoutingMiddleware
from src.notes_system import models as notes_models
from src.notes_system.api import router as notes_router
from src.video_analysis import models as video_models
from src.video_analysis.api import router as video_router

# Create a FastAPI app for testing
app = FastAPI()
app.add_middleware(SchemaRoutingMiddleware)
app.include_router(notes_router, prefix="/notes_system", tags=["notes_system"])
app.include_router(video_router, prefix="/video_analysis", tags=["video_analysis"])


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_db() -> AsyncGenerator[SchemaAwareDatabase, None]:
    """
    Fixture to create a test database and manage schemas.
    """
    test_schemas = ["tenant_a", "tenant_b"]
    all_metadata = [notes_models.Base.metadata, video_models.Base.metadata]

    async with db.engine.begin() as conn:
        # Create schemas
        for schema in test_schemas:
            await conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))

        # Create all tables in each schema
        for schema in test_schemas:
            await conn.execute(text(f'SET search_path TO "{schema}"'))
            for metadata in all_metadata:
                await conn.run_sync(metadata.create_all)

    yield db

    # Teardown
    async with db.engine.begin() as conn:
        for schema in test_schemas:
            await conn.execute(text(f'DROP SCHEMA IF EXISTS "{schema}" CASCADE'))


@pytest.fixture
async def db_session(test_db: SchemaAwareDatabase) -> AsyncGenerator[AsyncSession, None]:
    """
    Fixture to get a database session for a test.
    """
    async with test_db.get_session() as session:
        yield session


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture for a test client.
    """
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c