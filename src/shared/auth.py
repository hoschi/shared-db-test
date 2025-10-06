from pydantic import BaseModel


class User(BaseModel):
    """
    A simple user model for authentication purposes.
    """
    id: int
    username: str
    roles: list[str] = []


def get_current_user() -> User:
    """
    Placeholder function to simulate getting the current authenticated user.
    In a real application, this would involve token validation.
    For testing purposes, we can return a default user.
    """
    return User(id=1, username="testuser", roles=["admin"])