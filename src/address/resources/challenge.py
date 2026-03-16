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
from ..types.challenge_retrieve_response import ChallengeRetrieveResponse

__all__ = ["ChallengeResource", "AsyncChallengeResource"]


class ChallengeResource(SyncAPIResource):
    """
    Health, API information, and API key onboarding endpoints that do not require authentication.
    """

    @cached_property
    def with_raw_response(self) -> ChallengeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return ChallengeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChallengeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return ChallengeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChallengeRetrieveResponse:
        """
        Returns a cryptographic challenge for proof-of-work based API key registration.
        The challenge must be solved by finding a nonce that, when combined with the
        challenge data, produces a hash below the difficulty threshold. Use this
        challenge with the POST /request-key endpoint to obtain an API key.
        """
        return self._get(
            "/challenge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ChallengeRetrieveResponse,
        )


class AsyncChallengeResource(AsyncAPIResource):
    """
    Health, API information, and API key onboarding endpoints that do not require authentication.
    """

    @cached_property
    def with_raw_response(self) -> AsyncChallengeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/et0and/address-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChallengeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChallengeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/et0and/address-python#with_streaming_response
        """
        return AsyncChallengeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChallengeRetrieveResponse:
        """
        Returns a cryptographic challenge for proof-of-work based API key registration.
        The challenge must be solved by finding a nonce that, when combined with the
        challenge data, produces a hash below the difficulty threshold. Use this
        challenge with the POST /request-key endpoint to obtain an API key.
        """
        return await self._get(
            "/challenge",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=ChallengeRetrieveResponse,
        )


class ChallengeResourceWithRawResponse:
    def __init__(self, challenge: ChallengeResource) -> None:
        self._challenge = challenge

        self.retrieve = to_raw_response_wrapper(
            challenge.retrieve,
        )


class AsyncChallengeResourceWithRawResponse:
    def __init__(self, challenge: AsyncChallengeResource) -> None:
        self._challenge = challenge

        self.retrieve = async_to_raw_response_wrapper(
            challenge.retrieve,
        )


class ChallengeResourceWithStreamingResponse:
    def __init__(self, challenge: ChallengeResource) -> None:
        self._challenge = challenge

        self.retrieve = to_streamed_response_wrapper(
            challenge.retrieve,
        )


class AsyncChallengeResourceWithStreamingResponse:
    def __init__(self, challenge: AsyncChallengeResource) -> None:
        self._challenge = challenge

        self.retrieve = async_to_streamed_response_wrapper(
            challenge.retrieve,
        )
