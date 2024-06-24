# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import order_buy_params, order_open_params, order_sell_params
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
from ..types.order_buy_response import OrderBuyResponse
from ..types.order_open_response import OrderOpenResponse
from ..types.order_sell_response import OrderSellResponse

__all__ = ["OrdersResource", "AsyncOrdersResource"]


class OrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self)

    def buy(
        self,
        *,
        price: float | NotGiven = NOT_GIVEN,
        quantity: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderBuyResponse:
        """
        Place a buy order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/orders/buy",
            body=maybe_transform(
                {
                    "price": price,
                    "quantity": quantity,
                    "symbol": symbol,
                },
                order_buy_params.OrderBuyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderBuyResponse,
        )

    def open(
        self,
        *,
        symbol: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderOpenResponse:
        """
        Retrieve open orders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/orders/open",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbol": symbol}, order_open_params.OrderOpenParams),
            ),
            cast_to=OrderOpenResponse,
        )

    def sell(
        self,
        *,
        price: float | NotGiven = NOT_GIVEN,
        quantity: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderSellResponse:
        """
        Place a sell order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/orders/sell",
            body=maybe_transform(
                {
                    "price": price,
                    "quantity": quantity,
                    "symbol": symbol,
                },
                order_sell_params.OrderSellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderSellResponse,
        )


class AsyncOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self)

    async def buy(
        self,
        *,
        price: float | NotGiven = NOT_GIVEN,
        quantity: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderBuyResponse:
        """
        Place a buy order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/orders/buy",
            body=await async_maybe_transform(
                {
                    "price": price,
                    "quantity": quantity,
                    "symbol": symbol,
                },
                order_buy_params.OrderBuyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderBuyResponse,
        )

    async def open(
        self,
        *,
        symbol: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderOpenResponse:
        """
        Retrieve open orders

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/orders/open",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbol": symbol}, order_open_params.OrderOpenParams),
            ),
            cast_to=OrderOpenResponse,
        )

    async def sell(
        self,
        *,
        price: float | NotGiven = NOT_GIVEN,
        quantity: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderSellResponse:
        """
        Place a sell order

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/orders/sell",
            body=await async_maybe_transform(
                {
                    "price": price,
                    "quantity": quantity,
                    "symbol": symbol,
                },
                order_sell_params.OrderSellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderSellResponse,
        )


class OrdersResourceWithRawResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.buy = to_raw_response_wrapper(
            orders.buy,
        )
        self.open = to_raw_response_wrapper(
            orders.open,
        )
        self.sell = to_raw_response_wrapper(
            orders.sell,
        )


class AsyncOrdersResourceWithRawResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.buy = async_to_raw_response_wrapper(
            orders.buy,
        )
        self.open = async_to_raw_response_wrapper(
            orders.open,
        )
        self.sell = async_to_raw_response_wrapper(
            orders.sell,
        )


class OrdersResourceWithStreamingResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.buy = to_streamed_response_wrapper(
            orders.buy,
        )
        self.open = to_streamed_response_wrapper(
            orders.open,
        )
        self.sell = to_streamed_response_wrapper(
            orders.sell,
        )


class AsyncOrdersResourceWithStreamingResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.buy = async_to_streamed_response_wrapper(
            orders.buy,
        )
        self.open = async_to_streamed_response_wrapper(
            orders.open,
        )
        self.sell = async_to_streamed_response_wrapper(
            orders.sell,
        )
