# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import AddressError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.get_api_info_response import GetAPIInfoResponse

if TYPE_CHECKING:
    from .resources import meta, health, search, reverse, addresses, challenge, request_key
    from .resources.meta import MetaResource, AsyncMetaResource
    from .resources.health import HealthResource, AsyncHealthResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.reverse import ReverseResource, AsyncReverseResource
    from .resources.addresses import AddressesResource, AsyncAddressesResource
    from .resources.challenge import ChallengeResource, AsyncChallengeResource
    from .resources.request_key import RequestKeyResource, AsyncRequestKeyResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Address", "AsyncAddress", "Client", "AsyncClient"]


class Address(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Address client instance.

        This automatically infers the `api_key` argument from the `ADDRESS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ADDRESS_API_KEY")
        if api_key is None:
            raise AddressError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ADDRESS_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ADDRESS_BASE_URL")
        if base_url is None:
            base_url = f"https://address.tom.so"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> HealthResource:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.health import HealthResource

        return HealthResource(self)

    @cached_property
    def challenge(self) -> ChallengeResource:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.challenge import ChallengeResource

        return ChallengeResource(self)

    @cached_property
    def request_key(self) -> RequestKeyResource:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.request_key import RequestKeyResource

        return RequestKeyResource(self)

    @cached_property
    def addresses(self) -> AddressesResource:
        """
        Look up and list NZ addresses with filtering, pagination, and address ID lookup.
        """
        from .resources.addresses import AddressesResource

        return AddressesResource(self)

    @cached_property
    def search(self) -> SearchResource:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def reverse(self) -> ReverseResource:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.reverse import ReverseResource

        return ReverseResource(self)

    @cached_property
    def meta(self) -> MetaResource:
        """Dataset version, ingestion status, and service metadata."""
        from .resources.meta import MetaResource

        return MetaResource(self)

    @cached_property
    def with_raw_response(self) -> AddressWithRawResponse:
        return AddressWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressWithStreamedResponse:
        return AddressWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def get_api_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetAPIInfoResponse:
        """
        Returns basic API information including available endpoints and version details.
        This is the entry point for discovering the API capabilities.
        """
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=GetAPIInfoResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncAddress(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncAddress client instance.

        This automatically infers the `api_key` argument from the `ADDRESS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ADDRESS_API_KEY")
        if api_key is None:
            raise AddressError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ADDRESS_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ADDRESS_BASE_URL")
        if base_url is None:
            base_url = f"https://address.tom.so"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def health(self) -> AsyncHealthResource:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.health import AsyncHealthResource

        return AsyncHealthResource(self)

    @cached_property
    def challenge(self) -> AsyncChallengeResource:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.challenge import AsyncChallengeResource

        return AsyncChallengeResource(self)

    @cached_property
    def request_key(self) -> AsyncRequestKeyResource:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.request_key import AsyncRequestKeyResource

        return AsyncRequestKeyResource(self)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        """
        Look up and list NZ addresses with filtering, pagination, and address ID lookup.
        """
        from .resources.addresses import AsyncAddressesResource

        return AsyncAddressesResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def reverse(self) -> AsyncReverseResource:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.reverse import AsyncReverseResource

        return AsyncReverseResource(self)

    @cached_property
    def meta(self) -> AsyncMetaResource:
        """Dataset version, ingestion status, and service metadata."""
        from .resources.meta import AsyncMetaResource

        return AsyncMetaResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncAddressWithRawResponse:
        return AsyncAddressWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressWithStreamedResponse:
        return AsyncAddressWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._api_key if security.get("api_key", False) else {}),
        }

    @property
    def _api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def get_api_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetAPIInfoResponse:
        """
        Returns basic API information including available endpoints and version details.
        This is the entry point for discovering the API capabilities.
        """
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=GetAPIInfoResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AddressWithRawResponse:
    _client: Address

    def __init__(self, client: Address) -> None:
        self._client = client

        self.get_api_info = to_raw_response_wrapper(
            client.get_api_info,
        )

    @cached_property
    def health(self) -> health.HealthResourceWithRawResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.health import HealthResourceWithRawResponse

        return HealthResourceWithRawResponse(self._client.health)

    @cached_property
    def challenge(self) -> challenge.ChallengeResourceWithRawResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.challenge import ChallengeResourceWithRawResponse

        return ChallengeResourceWithRawResponse(self._client.challenge)

    @cached_property
    def request_key(self) -> request_key.RequestKeyResourceWithRawResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.request_key import RequestKeyResourceWithRawResponse

        return RequestKeyResourceWithRawResponse(self._client.request_key)

    @cached_property
    def addresses(self) -> addresses.AddressesResourceWithRawResponse:
        """
        Look up and list NZ addresses with filtering, pagination, and address ID lookup.
        """
        from .resources.addresses import AddressesResourceWithRawResponse

        return AddressesResourceWithRawResponse(self._client.addresses)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def reverse(self) -> reverse.ReverseResourceWithRawResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.reverse import ReverseResourceWithRawResponse

        return ReverseResourceWithRawResponse(self._client.reverse)

    @cached_property
    def meta(self) -> meta.MetaResourceWithRawResponse:
        """Dataset version, ingestion status, and service metadata."""
        from .resources.meta import MetaResourceWithRawResponse

        return MetaResourceWithRawResponse(self._client.meta)


class AsyncAddressWithRawResponse:
    _client: AsyncAddress

    def __init__(self, client: AsyncAddress) -> None:
        self._client = client

        self.get_api_info = async_to_raw_response_wrapper(
            client.get_api_info,
        )

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithRawResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.health import AsyncHealthResourceWithRawResponse

        return AsyncHealthResourceWithRawResponse(self._client.health)

    @cached_property
    def challenge(self) -> challenge.AsyncChallengeResourceWithRawResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.challenge import AsyncChallengeResourceWithRawResponse

        return AsyncChallengeResourceWithRawResponse(self._client.challenge)

    @cached_property
    def request_key(self) -> request_key.AsyncRequestKeyResourceWithRawResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.request_key import AsyncRequestKeyResourceWithRawResponse

        return AsyncRequestKeyResourceWithRawResponse(self._client.request_key)

    @cached_property
    def addresses(self) -> addresses.AsyncAddressesResourceWithRawResponse:
        """
        Look up and list NZ addresses with filtering, pagination, and address ID lookup.
        """
        from .resources.addresses import AsyncAddressesResourceWithRawResponse

        return AsyncAddressesResourceWithRawResponse(self._client.addresses)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def reverse(self) -> reverse.AsyncReverseResourceWithRawResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.reverse import AsyncReverseResourceWithRawResponse

        return AsyncReverseResourceWithRawResponse(self._client.reverse)

    @cached_property
    def meta(self) -> meta.AsyncMetaResourceWithRawResponse:
        """Dataset version, ingestion status, and service metadata."""
        from .resources.meta import AsyncMetaResourceWithRawResponse

        return AsyncMetaResourceWithRawResponse(self._client.meta)


class AddressWithStreamedResponse:
    _client: Address

    def __init__(self, client: Address) -> None:
        self._client = client

        self.get_api_info = to_streamed_response_wrapper(
            client.get_api_info,
        )

    @cached_property
    def health(self) -> health.HealthResourceWithStreamingResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.health import HealthResourceWithStreamingResponse

        return HealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def challenge(self) -> challenge.ChallengeResourceWithStreamingResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.challenge import ChallengeResourceWithStreamingResponse

        return ChallengeResourceWithStreamingResponse(self._client.challenge)

    @cached_property
    def request_key(self) -> request_key.RequestKeyResourceWithStreamingResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.request_key import RequestKeyResourceWithStreamingResponse

        return RequestKeyResourceWithStreamingResponse(self._client.request_key)

    @cached_property
    def addresses(self) -> addresses.AddressesResourceWithStreamingResponse:
        """
        Look up and list NZ addresses with filtering, pagination, and address ID lookup.
        """
        from .resources.addresses import AddressesResourceWithStreamingResponse

        return AddressesResourceWithStreamingResponse(self._client.addresses)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def reverse(self) -> reverse.ReverseResourceWithStreamingResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.reverse import ReverseResourceWithStreamingResponse

        return ReverseResourceWithStreamingResponse(self._client.reverse)

    @cached_property
    def meta(self) -> meta.MetaResourceWithStreamingResponse:
        """Dataset version, ingestion status, and service metadata."""
        from .resources.meta import MetaResourceWithStreamingResponse

        return MetaResourceWithStreamingResponse(self._client.meta)


class AsyncAddressWithStreamedResponse:
    _client: AsyncAddress

    def __init__(self, client: AsyncAddress) -> None:
        self._client = client

        self.get_api_info = async_to_streamed_response_wrapper(
            client.get_api_info,
        )

    @cached_property
    def health(self) -> health.AsyncHealthResourceWithStreamingResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.health import AsyncHealthResourceWithStreamingResponse

        return AsyncHealthResourceWithStreamingResponse(self._client.health)

    @cached_property
    def challenge(self) -> challenge.AsyncChallengeResourceWithStreamingResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.challenge import AsyncChallengeResourceWithStreamingResponse

        return AsyncChallengeResourceWithStreamingResponse(self._client.challenge)

    @cached_property
    def request_key(self) -> request_key.AsyncRequestKeyResourceWithStreamingResponse:
        """
        Health, API information, and API key onboarding endpoints that do not require authentication.
        """
        from .resources.request_key import AsyncRequestKeyResourceWithStreamingResponse

        return AsyncRequestKeyResourceWithStreamingResponse(self._client.request_key)

    @cached_property
    def addresses(self) -> addresses.AsyncAddressesResourceWithStreamingResponse:
        """
        Look up and list NZ addresses with filtering, pagination, and address ID lookup.
        """
        from .resources.addresses import AsyncAddressesResourceWithStreamingResponse

        return AsyncAddressesResourceWithStreamingResponse(self._client.addresses)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def reverse(self) -> reverse.AsyncReverseResourceWithStreamingResponse:
        """
        Full-text address search and reverse geocoding powered by FTS5 with abbreviation expansion.
        """
        from .resources.reverse import AsyncReverseResourceWithStreamingResponse

        return AsyncReverseResourceWithStreamingResponse(self._client.reverse)

    @cached_property
    def meta(self) -> meta.AsyncMetaResourceWithStreamingResponse:
        """Dataset version, ingestion status, and service metadata."""
        from .resources.meta import AsyncMetaResourceWithStreamingResponse

        return AsyncMetaResourceWithStreamingResponse(self._client.meta)


Client = Address

AsyncClient = AsyncAddress
