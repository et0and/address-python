# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from address import Address, AsyncAddress
from tests.utils import assert_matches_type
from address.types import ReverseGeocodeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReverse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_geocode(self, client: Address) -> None:
        reverse = client.reverse.geocode(
            point="point",
        )
        assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_geocode_with_all_params(self, client: Address) -> None:
        reverse = client.reverse.geocode(
            point="point",
            format="format",
            limit="limit",
        )
        assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_geocode(self, client: Address) -> None:
        response = client.reverse.with_raw_response.geocode(
            point="point",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reverse = response.parse()
        assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_geocode(self, client: Address) -> None:
        with client.reverse.with_streaming_response.geocode(
            point="point",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reverse = response.parse()
            assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReverse:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_geocode(self, async_client: AsyncAddress) -> None:
        reverse = await async_client.reverse.geocode(
            point="point",
        )
        assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_geocode_with_all_params(self, async_client: AsyncAddress) -> None:
        reverse = await async_client.reverse.geocode(
            point="point",
            format="format",
            limit="limit",
        )
        assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_geocode(self, async_client: AsyncAddress) -> None:
        response = await async_client.reverse.with_raw_response.geocode(
            point="point",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reverse = await response.parse()
        assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_geocode(self, async_client: AsyncAddress) -> None:
        async with async_client.reverse.with_streaming_response.geocode(
            point="point",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reverse = await response.parse()
            assert_matches_type(ReverseGeocodeResponse, reverse, path=["response"])

        assert cast(Any, response.is_closed) is True
