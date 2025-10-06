import pytest
from unittest.mock import patch, AsyncMock

from fastapi import HTTPException

from src.notes_system.api import get_note, create_note, NoteIn
from src.video_analysis.api import get_video, create_video, VideoIn
from src.notes_system import models as notes_models
from src.video_analysis import models as video_models


@pytest.mark.asyncio
async def test_get_note_not_found():
    """
    Tests that get_note raises a 404 HTTPException when the note is not found.
    """
    with patch('src.notes_system.services.get_note', new_callable=AsyncMock) as mock_get_note:
        mock_get_note.return_value = None
        mock_session = AsyncMock()

        with pytest.raises(HTTPException) as exc_info:
            await get_note(note_id=1, session=mock_session)

        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Note not found"


@pytest.mark.asyncio
async def test_create_note_endpoint():
    """
    Tests the create_note endpoint.
    """
    with patch('src.notes_system.services.create_note', new_callable=AsyncMock) as mock_create_note:
        note_in = NoteIn(title="Test", content="Test content")
        mock_session = AsyncMock()
        mock_create_note.return_value = notes_models.Note(id=1, title=note_in.title, content_markdown=note_in.content)

        result = await create_note(note=note_in, session=mock_session)

        mock_create_note.assert_awaited_once_with(mock_session, note_in.title, note_in.content)
        assert result.title == note_in.title


@pytest.mark.asyncio
async def test_get_video_not_found():
    """
    Tests that get_video raises a 404 HTTPException when the video is not found.
    """
    with patch('src.video_analysis.services.get_video', new_callable=AsyncMock) as mock_get_video:
        mock_get_video.return_value = None
        mock_session = AsyncMock()

        with pytest.raises(HTTPException) as exc_info:
            await get_video(video_id=1, session=mock_session)

        assert exc_info.value.status_code == 404
        assert exc_info.value.detail == "Video not found"


@pytest.mark.asyncio
async def test_create_video_endpoint():
    """
    Tests the create_video endpoint.
    """
    with patch('src.video_analysis.services.create_video', new_callable=AsyncMock) as mock_create_video:
        video_in = VideoIn(youtube_id="testid", title="Test Video")
        mock_session = AsyncMock()
        mock_create_video.return_value = video_models.Video(id=1, youtube_video_id=video_in.youtube_id, title=video_in.title)

        result = await create_video(video=video_in, session=mock_session)

        mock_create_video.assert_awaited_once_with(mock_session, video_in.youtube_id, video_in.title)
        assert result.title == video_in.title