import pytest
from unittest.mock import patch, AsyncMock

from src.core.database import db


@pytest.mark.asyncio
async def test_get_session_handles_exception():
    """
    Tests that the get_session context manager correctly handles exceptions
    and ensures the session is rolled back and closed.
    """
    # Mock the session factory to return a mock session
    mock_session = AsyncMock()
    mock_session.rollback = AsyncMock()
    mock_session.close = AsyncMock()
    mock_session.execute = AsyncMock()

    # We patch the session_factory on the 'db' instance
    with patch.object(db, 'session_factory', return_value=mock_session):
        with pytest.raises(ValueError, match="Test exception"):
            # We call the actual get_session method, which will now use our mock session
            async with db.get_session() as session:
                assert session is mock_session
                raise ValueError("Test exception")

        # The rollback should have been called in the 'except' block of get_session
        mock_session.rollback.assert_awaited_once()
        # The close should have been called in the 'finally' block
        mock_session.close.assert_awaited_once()