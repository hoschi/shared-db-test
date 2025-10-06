import pytest
from unittest.mock import AsyncMock, MagicMock

from src.notes_system import services as notes_services
from src.notes_system import models as notes_models
from src.video_analysis import services as video_services
from src.video_analysis import models as video_models

@pytest.mark.asyncio
async def test_create_note():
    mock_session = AsyncMock()
    mock_session.add = MagicMock() # Fix: 'add' is not an async method
    title = "Test Note"
    content = "Test Content"

    created_note = await notes_services.create_note(mock_session, title, content)

    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()
    assert isinstance(created_note, notes_models.Note)
    assert created_note.title == title
    assert created_note.content_markdown == content

@pytest.mark.asyncio
async def test_get_note():
    mock_session = AsyncMock()
    note_id = 1

    await notes_services.get_note(mock_session, note_id)

    mock_session.get.assert_awaited_once_with(notes_models.Note, note_id)

@pytest.mark.asyncio
async def test_create_video():
    mock_session = AsyncMock()
    mock_session.add = MagicMock() # Fix: 'add' is not an async method
    youtube_id = "testid"
    title = "Test Video"

    created_video = await video_services.create_video(mock_session, youtube_id, title)

    mock_session.add.assert_called_once()
    mock_session.flush.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()
    assert isinstance(created_video, video_models.Video)
    assert created_video.youtube_video_id == youtube_id
    assert created_video.title == title

@pytest.mark.asyncio
async def test_get_video():
    mock_session = AsyncMock()
    video_id = 1

    await video_services.get_video(mock_session, video_id)

    mock_session.get.assert_awaited_once_with(video_models.Video, video_id)