from __future__ import annotations

from pydantic import BaseModel, Field


class WsoProperty(BaseModel):
    """Represents "wso" property."""

    fidp: str = Field(..., alias='fidp')
    login_url: str = Field(..., alias='loginUrl')
    logout_url: str = Field(..., alias='logoutUrl')
    logout_success_url: str = Field(..., alias='logoutSuccessUrl')
    silent_redirect_url: str = Field(..., alias='silentRedirectUrl')
    redirect_url: str = Field(..., alias='redirectUrl')
    client_id: str = Field(..., alias='clientId')
    issuer: str = Field(..., alias='issuer')


class AppConfigJSON(BaseModel):
    """Represents app.config.json file configuration."""

    # NOTE:
    #   [DOCS] original "backend.host"
    #   has been reduced to "backend_host" for simplicity.
    wso: WsoProperty
    # backend_host: str
