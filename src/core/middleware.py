from contextvars import ContextVar
from typing import Awaitable, Callable

from fastapi import Request, Response

# Context variable to hold the schema for the current request context.
# The default value 'public' is used if no schema is specified.
schema_context: ContextVar[str] = ContextVar("schema_context", default="public")


class SchemaRoutingMiddleware:
    """
    FastAPI middleware to route database connections to the appropriate schema.
    It inspects the `X-Schema-Name` header of incoming requests.
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        """
        Processes the incoming request to set the schema context.
        """
        # Get schema from the header. Fallback to 'public' if not present.
        schema_name = request.headers.get("X-Schema-Name", "public")

        # Set the schema name in the context variable for this request.
        token = schema_context.set(schema_name)

        # Process the request.
        response = await call_next(request)

        # Reset the context variable to its previous state.
        schema_context.reset(token)

        return response