from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
if TYPE_CHECKING:
    from models.item import Item


@pymongo
@jsonclass
class Statement(BaseObject):
    name: str = types.str.required
    user_id: str = types.str.required
    office: str = types.str.required
    date_range: str = types.str.required
    client: str = types.str.required
    client_address: str = types.str.required
    package: str = types.str.required
    total_due: int = types.int.required
    due_date: datetime = types.datetime.required
    biller_coder: int = types.int.required
    ref: int = types.int.required
    payment_terms: str = types.str.required
    customer_number: str = types.str.required
    customer_name: str = types.str.required
    items: list[Item] = types.nonnull.listof('Item').linkedby('statement')