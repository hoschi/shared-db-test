import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_schema_isolation_for_notes(client: AsyncClient, test_db):
    """
    Tests that data created in one schema is not accessible from another.
    """
    # 1. Create a note in tenant_a's schema
    headers_a = {"X-Schema-Name": "tenant_a"}
    note_data = {"title": "Note A", "content": "This is a note for tenant A."}
    response_a = await client.post("/notes_system/notes/", json=note_data, headers=headers_a)
    assert response_a.status_code == 200
    note_a_id = response_a.json()["id"]

    # 2. Verify the note can be retrieved from tenant_a
    response_get_a = await client.get(f"/notes_system/notes/{note_a_id}", headers=headers_a)
    assert response_get_a.status_code == 200
    assert response_get_a.json()["title"] == "Note A"

    # 3. Attempt to retrieve the note from tenant_b's schema
    headers_b = {"X-Schema-Name": "tenant_b"}
    response_get_b = await client.get(f"/notes_system/notes/{note_a_id}", headers=headers_b)

    # 4. Assert that the note is not found in tenant_b
    # The current implementation of get_note returns the object or None.
    # FastAPI/Starlette will turn a None response into a 404 if the response model isn't optional,
    # but since our service returns None and the endpoint doesn't handle it, we expect a 500 error
    # from Pydantic validation failing on a None object.
    # A more robust implementation would return a 404. For this test, we accept 500.
    assert response_get_b.status_code == 404


@pytest.mark.asyncio
async def test_schema_isolation_for_videos(client: AsyncClient, test_db):
    """
    Tests that video data created in one schema is not accessible from another.
    """
    # 1. Create a video in tenant_b's schema
    headers_b = {"X-Schema-Name": "tenant_b"}
    video_data = {"youtube_id": "dQw4w9WgXcQ", "title": "Test Video B"}
    response_b = await client.post("/video_analysis/videos/", json=video_data, headers=headers_b)
    assert response_b.status_code == 200
    video_b_id = response_b.json()["id"]

    # 2. Verify the video can be retrieved from tenant_b
    response_get_b = await client.get(f"/video_analysis/videos/{video_b_id}", headers=headers_b)
    assert response_get_b.status_code == 200
    assert response_get_b.json()["title"] == "Test Video B"

    # 3. Attempt to retrieve the video from tenant_a's schema
    headers_a = {"X-Schema-Name": "tenant_a"}
    response_get_a = await client.get(f"/video_analysis/videos/{video_b_id}", headers=headers_a)

    # 4. Assert that the video is not found in tenant_a
    assert response_get_a.status_code == 404