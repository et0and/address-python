# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import request_key_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.request_key_create_response import RequestKeyCreateResponse

__all__ = ["RequestKeyResource", "AsyncRequestKeyResource"]


class RequestKeyResource(SyncAPIResource):
    """
    Health, API information, and API key onboarding endpoints that do not require authentication.
    """

    @cached_property
    def with_raw_response(self) -> RequestKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return RequestKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return RequestKeyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        token: str,
        challenge: str,
        nonce: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestKeyCreateResponse:
        """Submit a proof-of-work solution to obtain an API key.

        The request must include a
        valid nonce that solves the challenge previously obtained from GET /challenge.
        This prevents automated abuse while allowing legitimate users to access the API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/request-key",
            body=maybe_transform(
                {
                    "token": token,
                    "challenge": challenge,
                    "nonce": nonce,
                },
                request_key_create_params.RequestKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=RequestKeyCreateResponse,
        )


class AsyncRequestKeyResource(AsyncAPIResource):
    """
    Health, API information, and API key onboarding endpoints that do not require authentication.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRequestKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return AsyncRequestKeyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        token: str,
        challenge: str,
        nonce: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RequestKeyCreateResponse:
        """Submit a proof-of-work solution to obtain an API key.

        The request must include a
        valid nonce that solves the challenge previously obtained from GET /challenge.
        This prevents automated abuse while allowing legitimate users to access the API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/request-key",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "challenge": challenge,
                    "nonce": nonce,
                },
                request_key_create_params.RequestKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=RequestKeyCreateResponse,
        )


class RequestKeyResourceWithRawResponse:
    def __init__(self, request_key: RequestKeyResource) -> None:
        self._request_key = request_key

        self.create = to_raw_response_wrapper(
            request_key.create,
        )


class AsyncRequestKeyResourceWithRawResponse:
    def __init__(self, request_key: AsyncRequestKeyResource) -> None:
        self._request_key = request_key

        self.create = async_to_raw_response_wrapper(
            request_key.create,
        )


class RequestKeyResourceWithStreamingResponse:
    def __init__(self, request_key: RequestKeyResource) -> None:
        self._request_key = request_key

        self.create = to_streamed_response_wrapper(
            request_key.create,
        )


class AsyncRequestKeyResourceWithStreamingResponse:
    def __init__(self, request_key: AsyncRequestKeyResource) -> None:
        self._request_key = request_key

        self.create = async_to_streamed_response_wrapper(
            request_key.create,
        )
