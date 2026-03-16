# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetaRetrieveResponse"]


class MetaRetrieveResponse(BaseModel):
    last_updated: str = FieldInfo(alias="lastUpdated")

    total_addresses: float = FieldInfo(alias="totalAddresses")

    version: str
