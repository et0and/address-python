# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchQueryParams"]


class SearchQueryParams(TypedDict, total=False):
    q: Required[str]

    bbox: str

    format: str

    limit: str

    polygon: str
