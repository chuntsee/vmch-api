from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
if TYPE_CHECKING:
    from models.statement import Statement


@pymongo
@jsonclass
class Item(BaseObject):
    purchase_date: datetime = types.datetime.required
    ref_no: int = types.int.required
    description: str = types.str.required
    days: int = types.int.required
    rate: int = types.int.required
    amount: int = types.int.required
    balance: int = types.int.required
    statement: Statement = types.instanceof('Statement').linkto.required

