# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrderOpenResponse", "OrderOpenResponseItem"]


class OrderOpenResponseItem(BaseModel):
    order_id: Optional[str] = FieldInfo(alias="orderId", default=None)

    price: Optional[float] = None

    quantity: Optional[float] = None

    status: Optional[str] = None


OrderOpenResponse = List[OrderOpenResponseItem]
