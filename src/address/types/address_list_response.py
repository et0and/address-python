# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddressListResponse", "AddressListResponseItem"]


class AddressListResponseItem(BaseModel):
    address_id: float = FieldInfo(alias="addressId")

    full_address: str = FieldInfo(alias="fullAddress")

    full_address_number: str = FieldInfo(alias="fullAddressNumber")

    latitude: float

    longitude: float

    suburb: str

    territorial_authority: str = FieldInfo(alias="territorialAuthority")

    town_city: str = FieldInfo(alias="townCity")

    full_address_road: Optional[str] = FieldInfo(alias="fullAddressRoad", default=None)

    postcode: Optional[str] = None

    region: Optional[str] = None


AddressListResponse: TypeAlias = List[AddressListResponseItem]
