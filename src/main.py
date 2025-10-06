from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.middleware import SchemaRoutingMiddleware
from src.notes_system.api import router as notes_router
from src.video_analysis.api import router as video_router
from src.core.logging_config import setup_logging

@asynccontextmanager
async def lifespan(_: object) -> AsyncGenerator[None, None]:
    """
    Application lifespan context to set up logging.
    """
    setup_logging()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(SchemaRoutingMiddleware)
app.include_router(notes_router, prefix="/notes_system", tags=["notes_system"])
app.include_router(video_router, prefix="/video_analysis", tags=["video_analysis"])

@app.get("/")
async def read_root():
    return {"message": "Service is running"}