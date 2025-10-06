from sqlalchemy.ext.asyncio import AsyncSession

from . import models


async def create_note(session: AsyncSession, title: str, content: str) -> models.Note:
    """
    Creates a new note.
    """
    note = models.Note(title=title, content_markdown=content)
    session.add(note)
    await session.flush()
    await session.refresh(note)
    return note


async def get_note(session: AsyncSession, note_id: int) -> models.Note | None:
    """
    Retrieves a note by its ID.
    """
    note = await session.get(models.Note, note_id)
    return note