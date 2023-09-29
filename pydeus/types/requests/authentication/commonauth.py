from pydantic import BaseModel, Field


class CommonAuthBodyRequest(BaseModel):
    """Respresents a body data for a commonauth request."""

    saml_response: str = Field(..., alias='SAMLResponse')
    relay_state: str = Field(..., alias='RelayState')
