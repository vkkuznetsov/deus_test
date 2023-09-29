from pydantic import BaseModel, Field


class AdfsAuthenticationBodyRequest(BaseModel):
    """Represents a body data for authnection via adfs."""

    user_name: str = Field(..., alias='UserName')
    password: str = Field(..., alias='Password')
    auth_method: str = Field('FormsAuthentication', alias='AuthMethod')
