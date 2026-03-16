# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from address import Address, AsyncAddress
from tests.utils import assert_matches_type
from address.types import RequestKeyCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequestKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Address) -> None:
        request_key = client.request_key.create(
            token="token",
            challenge="challenge",
            nonce=0,
        )
        assert_matches_type(RequestKeyCreateResponse, request_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Address) -> None:
        response = client.request_key.with_raw_response.create(
            token="token",
            challenge="challenge",
            nonce=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_key = response.parse()
        assert_matches_type(RequestKeyCreateResponse, request_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Address) -> None:
        with client.request_key.with_streaming_response.create(
            token="token",
            challenge="challenge",
            nonce=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_key = response.parse()
            assert_matches_type(RequestKeyCreateResponse, request_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRequestKey:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAddress) -> None:
        request_key = await async_client.request_key.create(
            token="token",
            challenge="challenge",
            nonce=0,
        )
        assert_matches_type(RequestKeyCreateResponse, request_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAddress) -> None:
        response = await async_client.request_key.with_raw_response.create(
            token="token",
            challenge="challenge",
            nonce=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request_key = await response.parse()
        assert_matches_type(RequestKeyCreateResponse, request_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAddress) -> None:
        async with async_client.request_key.with_streaming_response.create(
            token="token",
            challenge="challenge",
            nonce=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request_key = await response.parse()
            assert_matches_type(RequestKeyCreateResponse, request_key, path=["response"])

        assert cast(Any, response.is_closed) is True
