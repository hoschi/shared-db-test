from sqlalchemy.ext.asyncio import AsyncSession

from . import models


async def create_video(session: AsyncSession, youtube_id: str, title: str) -> models.Video:
    """
    Creates a new video record.
    """
    video = models.Video(youtube_video_id=youtube_id, title=title)
    session.add(video)
    await session.flush()
    await session.refresh(video)
    return video


async def get_video(session: AsyncSession, video_id: int) -> models.Video | None:
    """
    Retrieves a video by its ID.
    """
    video = await session.get(models.Video, video_id)
    return video