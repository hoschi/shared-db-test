from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db_session
from . import models, services
from pydantic import BaseModel


class VideoIn(BaseModel):
    youtube_id: str
    title: str


class VideoOut(BaseModel):
    id: int
    youtube_video_id: str
    title: str

    class Config:
        orm_mode = True


router = APIRouter()


@router.post("/videos/", response_model=VideoOut)
async def create_video(
    video: VideoIn,
    session: AsyncSession = Depends(get_db_session),
):
    """
    Create a new video in the schema specified by the `X-Schema-Name` header.
    """
    created_video = await services.create_video(session, video.youtube_id, video.title)
    return created_video


@router.get("/videos/{video_id}", response_model=VideoOut)
async def get_video(
    video_id: int,
    session: AsyncSession = Depends(get_db_session),
):
    """
    Get a video by its ID from the schema specified by the `X-Schema-Name` header.
    """
    video = await services.get_video(session, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video