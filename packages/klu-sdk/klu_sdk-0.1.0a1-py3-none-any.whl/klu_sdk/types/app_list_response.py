# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["AppListResponse", "Data"]


class Data(BaseModel):
    created_by_id: str

    description: Optional[str] = None

    guid: str

    last_updated_by_id: Optional[str] = None

    name: str

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


class AppListResponse(BaseModel):
    data: List[Data]

    has_next_page: bool

    total_count: float
