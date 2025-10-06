import pytest
from unittest.mock import AsyncMock

from src.core.middleware import SchemaRoutingMiddleware, schema_context


@pytest.mark.asyncio
async def test_schema_routing_middleware():
    """
    Tests that the SchemaRoutingMiddleware correctly sets the schema context.
    """
    app = AsyncMock()
    middleware = SchemaRoutingMiddleware(app)

    # Test with a schema provided in the header
    scope_with_schema = {
        "type": "http",
        "headers": [(b"x-schema-name", b"test_schema")],
    }
    receive = AsyncMock()
    send = AsyncMock()

    await middleware(scope_with_schema, receive, send)

    # The app should have been called with the correct context
    app.assert_awaited_once()

    # To verify the context, we can check the context *during* the app call
    async def app_with_check(scope, receive, send):
        assert schema_context.get() == "test_schema"

    app.side_effect = app_with_check
    await middleware(scope_with_schema, receive, send)
    app.reset_mock() # Reset for the next test case

    # Test without a schema provided in the header (should default to 'public')
    scope_without_schema = {
        "type": "http",
        "headers": [],
    }

    async def app_with_default_check(scope, receive, send):
        assert schema_context.get() == "public"

    app.side_effect = app_with_default_check
    await middleware(scope_without_schema, receive, send)
    app.assert_awaited_once()
    app.reset_mock()

    # Test with a non-http scope
    scope_non_http = {"type": "websocket"}
    await middleware(scope_non_http, receive, send)
    app.assert_awaited_once_with(scope_non_http, receive, send)