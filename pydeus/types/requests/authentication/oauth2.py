from pydantic import BaseModel


class OAuth2QueryRequest(BaseModel):
    """Represents a query parameters for OAuth2 request."""

    client_id: str
    redirect_uri: str
    response_type: str = 'id_token'
    scope: str = 'openid'
    state: str
    nonce: str
