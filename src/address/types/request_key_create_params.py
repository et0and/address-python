# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RequestKeyCreateParams"]


class RequestKeyCreateParams(TypedDict, total=False):
    token: Required[str]

    challenge: Required[str]

    nonce: Required[float]
