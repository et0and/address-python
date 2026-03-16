# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.meta_retrieve_response import MetaRetrieveResponse

__all__ = ["MetaResource", "AsyncMetaResource"]


class MetaResource(SyncAPIResource):
    """Dataset version, ingestion status, and service metadata."""

    @cached_property
    def with_raw_response(self) -> MetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/address-python#accessing-raw-response-data-eg-headers
        """
        return MetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/address-python#with_streaming_response
        """
        return MetaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetaRetrieveResponse:
        """
        Returns metadata about the LINZ NZ Addresses dataset including:

        - Dataset version identifier
        - Last ingestion timestamp
        - Total record count
        - Data source information

        This endpoint is useful for client applications that need to verify data
        currency or display dataset attribution.
        """
        return self._get(
            "/v1/meta",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetaRetrieveResponse,
        )


class AsyncMetaResource(AsyncAPIResource):
    """Dataset version, ingestion status, and service metadata."""

    @cached_property
    def with_raw_response(self) -> AsyncMetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/address-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/address-python#with_streaming_response
        """
        return AsyncMetaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetaRetrieveResponse:
        """
        Returns metadata about the LINZ NZ Addresses dataset including:

        - Dataset version identifier
        - Last ingestion timestamp
        - Total record count
        - Data source information

        This endpoint is useful for client applications that need to verify data
        currency or display dataset attribution.
        """
        return await self._get(
            "/v1/meta",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetaRetrieveResponse,
        )


class MetaResourceWithRawResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

        self.retrieve = to_raw_response_wrapper(
            meta.retrieve,
        )


class AsyncMetaResourceWithRawResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

        self.retrieve = async_to_raw_response_wrapper(
            meta.retrieve,
        )


class MetaResourceWithStreamingResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

        self.retrieve = to_streamed_response_wrapper(
            meta.retrieve,
        )


class AsyncMetaResourceWithStreamingResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

        self.retrieve = async_to_streamed_response_wrapper(
            meta.retrieve,
        )
