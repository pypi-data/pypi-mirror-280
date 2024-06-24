# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import price_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.price_retrieve_response import PriceRetrieveResponse

__all__ = ["PricesResource", "AsyncPricesResource"]


class PricesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PricesResourceWithRawResponse:
        return PricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricesResourceWithStreamingResponse:
        return PricesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        symbol: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceRetrieveResponse:
        """
        Retrieve the current price of a trading pair

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbol": symbol}, price_retrieve_params.PriceRetrieveParams),
            ),
            cast_to=PriceRetrieveResponse,
        )


class AsyncPricesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPricesResourceWithRawResponse:
        return AsyncPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricesResourceWithStreamingResponse:
        return AsyncPricesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        symbol: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceRetrieveResponse:
        """
        Retrieve the current price of a trading pair

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbol": symbol}, price_retrieve_params.PriceRetrieveParams),
            ),
            cast_to=PriceRetrieveResponse,
        )


class PricesResourceWithRawResponse:
    def __init__(self, prices: PricesResource) -> None:
        self._prices = prices

        self.retrieve = to_raw_response_wrapper(
            prices.retrieve,
        )


class AsyncPricesResourceWithRawResponse:
    def __init__(self, prices: AsyncPricesResource) -> None:
        self._prices = prices

        self.retrieve = async_to_raw_response_wrapper(
            prices.retrieve,
        )


class PricesResourceWithStreamingResponse:
    def __init__(self, prices: PricesResource) -> None:
        self._prices = prices

        self.retrieve = to_streamed_response_wrapper(
            prices.retrieve,
        )


class AsyncPricesResourceWithStreamingResponse:
    def __init__(self, prices: AsyncPricesResource) -> None:
        self._prices = prices

        self.retrieve = async_to_streamed_response_wrapper(
            prices.retrieve,
        )
