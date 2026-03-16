# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from address import Address, AsyncAddress
from tests.utils import assert_matches_type
from address.types import MetaRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Address) -> None:
        meta = client.meta.retrieve()
        assert_matches_type(MetaRetrieveResponse, meta, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Address) -> None:
        response = client.meta.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = response.parse()
        assert_matches_type(MetaRetrieveResponse, meta, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Address) -> None:
        with client.meta.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = response.parse()
            assert_matches_type(MetaRetrieveResponse, meta, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAddress) -> None:
        meta = await async_client.meta.retrieve()
        assert_matches_type(MetaRetrieveResponse, meta, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAddress) -> None:
        response = await async_client.meta.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meta = await response.parse()
        assert_matches_type(MetaRetrieveResponse, meta, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAddress) -> None:
        async with async_client.meta.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meta = await response.parse()
            assert_matches_type(MetaRetrieveResponse, meta, path=["response"])

        assert cast(Any, response.is_closed) is True
