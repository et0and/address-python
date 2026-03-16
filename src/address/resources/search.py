# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import search_query_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_query_response import SearchQueryResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    """
    Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
    """

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def query(
        self,
        *,
        q: str,
        bbox: str | Omit = omit,
        format: str | Omit = omit,
        limit: str | Omit = omit,
        polygon: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchQueryResponse:
        """
        Search addresses using full-text search with intelligent query processing.

        **Search features:**

        - FTS5 full-text search with ranking by relevance
        - Automatic abbreviation expansion (e.g., "st" → "street", "rd" → "road")
        - Fuzzy matching fallback for typos and variations
        - Address component matching (street, suburb, city, postcode)

        **Query parameters:**

        - `q`: Search query string (required)
        - `limit`: Maximum results (default: 100, max: 1000)
        - `format`: Response format - "full" or "simple"

        **Examples:**

        - `/v1/search?q=lambton+quay` - Search for addresses on Lambton Quay
        - `/v1/search?q=123+quay+st+auckland` - Search for specific address
        - `/v1/search?q=wlg&limit=20` - Abbreviation expansion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "bbox": bbox,
                        "format": format,
                        "limit": limit,
                        "polygon": polygon,
                    },
                    search_query_params.SearchQueryParams,
                ),
            ),
            cast_to=SearchQueryResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    """
    Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def query(
        self,
        *,
        q: str,
        bbox: str | Omit = omit,
        format: str | Omit = omit,
        limit: str | Omit = omit,
        polygon: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchQueryResponse:
        """
        Search addresses using full-text search with intelligent query processing.

        **Search features:**

        - FTS5 full-text search with ranking by relevance
        - Automatic abbreviation expansion (e.g., "st" → "street", "rd" → "road")
        - Fuzzy matching fallback for typos and variations
        - Address component matching (street, suburb, city, postcode)

        **Query parameters:**

        - `q`: Search query string (required)
        - `limit`: Maximum results (default: 100, max: 1000)
        - `format`: Response format - "full" or "simple"

        **Examples:**

        - `/v1/search?q=lambton+quay` - Search for addresses on Lambton Quay
        - `/v1/search?q=123+quay+st+auckland` - Search for specific address
        - `/v1/search?q=wlg&limit=20` - Abbreviation expansion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "bbox": bbox,
                        "format": format,
                        "limit": limit,
                        "polygon": polygon,
                    },
                    search_query_params.SearchQueryParams,
                ),
            ),
            cast_to=SearchQueryResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.query = to_raw_response_wrapper(
            search.query,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.query = async_to_raw_response_wrapper(
            search.query,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.query = to_streamed_response_wrapper(
            search.query,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.query = async_to_streamed_response_wrapper(
            search.query,
        )
