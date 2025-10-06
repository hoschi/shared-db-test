import pytest
from unittest.mock import AsyncMock, Mock

from src.core.middleware import SchemaRoutingMiddleware, schema_context


@pytest.mark.asyncio
async def test_schema_routing_middleware():
    """
    Tests that the SchemaRoutingMiddleware correctly sets the schema context.
    """
    app = AsyncMock()
    middleware = SchemaRoutingMiddleware(app)

    # Test with a schema provided in the header
    request_with_schema = Mock()
    request_with_schema.headers = {"X-Schema-Name": "test_schema"}

    call_next = AsyncMock()

    await middleware(request_with_schema, call_next)

    # Check that the context was set correctly during the call
    # The context is reset after the call, so we can't check it directly.
    # Instead, we can check the value of the context variable inside the mock call

    # To do this, we can make the call_next mock check the context
    async def check_context(*args, **kwargs):
        assert schema_context.get() == "test_schema"

    call_next.side_effect = check_context
    await middleware(request_with_schema, call_next)


    # Test without a schema provided in the header (should default to 'public')
    request_without_schema = Mock()
    request_without_schema.headers = {}

    async def check_default_context(*args, **kwargs):
        assert schema_context.get() == "public"

    call_next.side_effect = check_default_context
    await middleware(request_without_schema, call_next)