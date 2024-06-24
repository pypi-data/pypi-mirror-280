# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrderSellParams"]


class OrderSellParams(TypedDict, total=False):
    price: float

    quantity: float

    symbol: str
