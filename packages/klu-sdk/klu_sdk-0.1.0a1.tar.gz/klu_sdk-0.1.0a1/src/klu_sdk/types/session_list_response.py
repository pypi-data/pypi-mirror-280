# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["SessionListResponse", "Data"]


class Data(BaseModel):
    action: str

    guid: str

    ext_user_id: Optional[str] = None

    name: Optional[str] = None


class SessionListResponse(BaseModel):
    data: List[Data]

    has_next_page: bool

    total_count: float
