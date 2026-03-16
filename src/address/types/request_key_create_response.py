# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RequestKeyCreateResponse"]


class RequestKeyCreateResponse(BaseModel):
    api_key: str = FieldInfo(alias="apiKey")

    rate_limit: float = FieldInfo(alias="rateLimit")
