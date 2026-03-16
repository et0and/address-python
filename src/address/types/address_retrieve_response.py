# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AddressRetrieveResponse"]


class AddressRetrieveResponse(BaseModel):
    address_id: float = FieldInfo(alias="addressId")

    full_address: str = FieldInfo(alias="fullAddress")

    full_address_number: str = FieldInfo(alias="fullAddressNumber")

    full_address_road: str = FieldInfo(alias="fullAddressRoad")

    latitude: float

    longitude: float

    postcode: str

    region: str

    suburb: str

    territorial_authority: str = FieldInfo(alias="territorialAuthority")

    town_city: str = FieldInfo(alias="townCity")
