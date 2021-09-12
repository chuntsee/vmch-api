from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from jsonclasses import jsonclass, types
from jsonclasses_pymongo import pymongo, BaseObject

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
    items: list[str] = types.listof(str).nonnull.required
    pending_items: list[str] = types.listof(str).nonnull.required