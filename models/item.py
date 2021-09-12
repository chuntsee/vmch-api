from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject
if TYPE_CHECKING:
    from models.statement import Statement
@pymongo
@jsonclass
class Item(BaseObject):
    name: str = types.str.required
    price: int = types.int.required
