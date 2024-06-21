# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Union, List, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["ContextListResponse", "ContextListResponseItem"]


class ContextListResponseItem(BaseModel):
    created_by_id: str = FieldInfo(alias="createdById")

    description: Optional[str] = None

    guid: str

    metadata: Union[str, float, bool, List[object], Dict[str, object], Optional[object]]

    name: str

    processed: bool

    created_at: Optional[object] = FieldInfo(alias="createdAt", default=None)

    updated_at: Optional[object] = FieldInfo(alias="updatedAt", default=None)


ContextListResponse = List[ContextListResponseItem]
