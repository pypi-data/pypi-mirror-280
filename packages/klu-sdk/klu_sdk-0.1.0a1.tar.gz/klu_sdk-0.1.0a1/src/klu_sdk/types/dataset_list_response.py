# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DatasetListResponse", "Data"]


class Data(BaseModel):
    app: str

    guid: str

    created_by_id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None


class DatasetListResponse(BaseModel):
    data: List[Data]

    has_next_page: bool

    total_count: float
