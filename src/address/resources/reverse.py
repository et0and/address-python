# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import reverse_geocode_params
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
from ..types.reverse_geocode_response import ReverseGeocodeResponse

__all__ = ["ReverseResource", "AsyncReverseResource"]


class ReverseResource(SyncAPIResource):
    """
    Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
    """

    @cached_property
    def with_raw_response(self) -> ReverseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/address-python#accessing-raw-response-data-eg-headers
        """
        return ReverseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReverseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/address-python#with_streaming_response
        """
        return ReverseResourceWithStreamingResponse(self)

    def geocode(
        self,
        *,
        point: str,
        format: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReverseGeocodeResponse:
        """
        Find the nearest addresses to given geographic coordinates (reverse geocoding).

        **Query parameters:**

        - `lat`: Latitude in decimal degrees (required)
        - `lng`: Longitude in decimal degrees (required)
        - `limit`: Maximum number of results (default: 10, max: 100)
        - `format`: Response format - "full" or "simple"

        **Distance calculation:** Results are sorted by distance from the provided
        coordinates, calculated using the Haversine formula for spherical distance on
        Earth.

        **Example:** `/v1/reverse?lat=-41.2865&lng=174.7762&limit=5`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "point": point,
                        "format": format,
                        "limit": limit,
                    },
                    reverse_geocode_params.ReverseGeocodeParams,
                ),
            ),
            cast_to=ReverseGeocodeResponse,
        )


class AsyncReverseResource(AsyncAPIResource):
    """
    Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
    """

    @cached_property
    def with_raw_response(self) -> AsyncReverseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/address-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReverseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReverseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/address-python#with_streaming_response
        """
        return AsyncReverseResourceWithStreamingResponse(self)

    async def geocode(
        self,
        *,
        point: str,
        format: str | Omit = omit,
        limit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReverseGeocodeResponse:
        """
        Find the nearest addresses to given geographic coordinates (reverse geocoding).

        **Query parameters:**

        - `lat`: Latitude in decimal degrees (required)
        - `lng`: Longitude in decimal degrees (required)
        - `limit`: Maximum number of results (default: 10, max: 100)
        - `format`: Response format - "full" or "simple"

        **Distance calculation:** Results are sorted by distance from the provided
        coordinates, calculated using the Haversine formula for spherical distance on
        Earth.

        **Example:** `/v1/reverse?lat=-41.2865&lng=174.7762&limit=5`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/reverse",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "point": point,
                        "format": format,
                        "limit": limit,
                    },
                    reverse_geocode_params.ReverseGeocodeParams,
                ),
            ),
            cast_to=ReverseGeocodeResponse,
        )


class ReverseResourceWithRawResponse:
    def __init__(self, reverse: ReverseResource) -> None:
        self._reverse = reverse

        self.geocode = to_raw_response_wrapper(
            reverse.geocode,
        )


class AsyncReverseResourceWithRawResponse:
    def __init__(self, reverse: AsyncReverseResource) -> None:
        self._reverse = reverse

        self.geocode = async_to_raw_response_wrapper(
            reverse.geocode,
        )


class ReverseResourceWithStreamingResponse:
    def __init__(self, reverse: ReverseResource) -> None:
        self._reverse = reverse

        self.geocode = to_streamed_response_wrapper(
            reverse.geocode,
        )


class AsyncReverseResourceWithStreamingResponse:
    def __init__(self, reverse: AsyncReverseResource) -> None:
        self._reverse = reverse

        self.geocode = async_to_streamed_response_wrapper(
            reverse.geocode,
        )
