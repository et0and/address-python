# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AddressListParams"]


class AddressListParams(TypedDict, total=False):
    bbox: str

    format: str

    limit: str

    offset: str

    road_name: str

    suburb_locality: str

    town_city: str
