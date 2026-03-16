# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ChallengeRetrieveResponse"]


class ChallengeRetrieveResponse(BaseModel):
    token: str

    challenge: str

    difficulty: float

    expires_at: float = FieldInfo(alias="expiresAt")
