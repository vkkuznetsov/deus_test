from pydantic import BaseModel


class Credentials(BaseModel):
    """A modeus credential model."""

    email: str
    password: str
    bearer: str = None
