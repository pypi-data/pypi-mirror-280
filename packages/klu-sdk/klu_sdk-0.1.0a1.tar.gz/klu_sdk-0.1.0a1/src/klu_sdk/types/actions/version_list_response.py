# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["VersionListResponse", "Data"]


class Data(BaseModel):
    created_by_id: str

    environments: List[str]

    guid: str

    version_number: float

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


class VersionListResponse(BaseModel):
    data: List[Data]

    has_next_page: bool

    total_count: float
