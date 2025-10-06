from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db_session
from . import models, services
from pydantic import BaseModel


class NoteIn(BaseModel):
    title: str
    content: str


class NoteOut(BaseModel):
    id: int
    title: str
    content_markdown: str

    class Config:
        orm_mode = True


router = APIRouter()


@router.post("/notes/", response_model=NoteOut)
async def create_note(
    note: NoteIn,
    session: AsyncSession = Depends(get_db_session),
):
    """
    Create a new note in the schema specified by the `X-Schema-Name` header.
    """
    created_note = await services.create_note(session, note.title, note.content)
    return created_note


@router.get("/notes/{note_id}", response_model=NoteOut)
async def get_note(
    note_id: int,
    session: AsyncSession = Depends(get_db_session),
):
    """
    Get a note by its ID from the schema specified by the `X-Schema-Name` header.
    """
    note = await services.get_note(session, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note