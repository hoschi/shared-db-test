from contextvars import ContextVar
from starlette.types import ASGIApp, Receive, Scope, Send


# Context variable to hold the schema for the current request context.
# The default value 'public' is used if no schema is specified.
schema_context: ContextVar[str] = ContextVar("schema_context", default="public")


class SchemaRoutingMiddleware:
    """
    FastAPI middleware to route database connections to the appropriate schema.
    It inspects the `X-Schema-Name` header of incoming requests.
    """

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
        Processes the incoming request to set the schema context.
        """
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        headers = scope.get("headers", [])
        schema_name = "public"
        for key, value in headers:
            if key.decode("latin-1") == "x-schema-name":
                schema_name = value.decode("latin-1")
                break

        token = schema_context.set(schema_name)
        await self.app(scope, receive, send)
        schema_context.reset(token)