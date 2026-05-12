# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import address_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.address_list_response import AddressListResponse
from ..types.address_retrieve_response import AddressRetrieveResponse

__all__ = ["AddressesResource", "AsyncAddressesResource"]


class AddressesResource(SyncAPIResource):
    """
    Look up and list NZ addresses with filtering, pagination, and address ID lookup.
    """

    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return AddressesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressRetrieveResponse:
        """
        Retrieve a single address record by its LINZ address_id.

        The address_id is a unique identifier assigned by Land Information New Zealand
        (LINZ). This is the canonical way to retrieve a specific address when you know
        its ID.

        **Response formats:**

        - Default: Full address object with all LINZ attributes
        - Simple (format=simple): Compact representation with essential fields only

        **Example:** `/v1/addresses/123456?format=simple`

        Args:
          id: a string to be decoded into a number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/addresses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressRetrieveResponse,
        )

    def list(
        self,
        *,
        bbox: str | Omit = omit,
        format: str | Omit = omit,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        road_name: str | Omit = omit,
        suburb_locality: str | Omit = omit,
        town_city: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressListResponse:
        """
        Retrieve a paginated list of addresses with optional filtering by location.

        **Filtering:**

        - `town_city`: Filter by town/city name (e.g., "Wellington")
        - `suburb_locality`: Filter by suburb/locality (e.g., "Te Aro")
        - `road_name`: Filter by road/street name (e.g., "Lambton Quay")
        - `bbox`: Bounding box filter as comma-separated coordinates
          (min_lon,min_lat,max_lon,max_lat)

        **Pagination:**

        - `limit`: Maximum number of results (default: 100, max: 1000)
        - `offset`: Number of results to skip

        **Example:** `/v1/addresses?town_city=Wellington&limit=50`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bbox": bbox,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                        "road_name": road_name,
                        "suburb_locality": suburb_locality,
                        "town_city": town_city,
                    },
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
        )


class AsyncAddressesResource(AsyncAPIResource):
    """
    Look up and list NZ addresses with filtering, pagination, and address ID lookup.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressRetrieveResponse:
        """
        Retrieve a single address record by its LINZ address_id.

        The address_id is a unique identifier assigned by Land Information New Zealand
        (LINZ). This is the canonical way to retrieve a specific address when you know
        its ID.

        **Response formats:**

        - Default: Full address object with all LINZ attributes
        - Simple (format=simple): Compact representation with essential fields only

        **Example:** `/v1/addresses/123456?format=simple`

        Args:
          id: a string to be decoded into a number

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/addresses/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressRetrieveResponse,
        )

    async def list(
        self,
        *,
        bbox: str | Omit = omit,
        format: str | Omit = omit,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        road_name: str | Omit = omit,
        suburb_locality: str | Omit = omit,
        town_city: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddressListResponse:
        """
        Retrieve a paginated list of addresses with optional filtering by location.

        **Filtering:**

        - `town_city`: Filter by town/city name (e.g., "Wellington")
        - `suburb_locality`: Filter by suburb/locality (e.g., "Te Aro")
        - `road_name`: Filter by road/street name (e.g., "Lambton Quay")
        - `bbox`: Bounding box filter as comma-separated coordinates
          (min_lon,min_lat,max_lon,max_lat)

        **Pagination:**

        - `limit`: Maximum number of results (default: 100, max: 1000)
        - `offset`: Number of results to skip

        **Example:** `/v1/addresses?town_city=Wellington&limit=50`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "bbox": bbox,
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                        "road_name": road_name,
                        "suburb_locality": suburb_locality,
                        "town_city": town_city,
                    },
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
        )


class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.retrieve = to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            addresses.list,
        )


class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.retrieve = async_to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            addresses.list,
        )


class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.retrieve = to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            addresses.list,
        )


class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.retrieve = async_to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            addresses.list,
        )
