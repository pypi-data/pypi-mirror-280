# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["AppListResponse", "AppListResponseItem"]


class AppListResponseItem(BaseModel):
    created_by_id: str

    guid: str

    name: str

    created_at: Optional[object] = None

    description: Optional[str] = None

    last_updated_by_id: Optional[str] = None

    updated_at: Optional[object] = None


AppListResponse = List[AppListResponseItem]
