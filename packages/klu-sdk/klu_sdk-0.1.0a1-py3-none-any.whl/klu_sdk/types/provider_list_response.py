# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["ProviderListResponse", "ProviderListResponseItem"]


class ProviderListResponseItem(BaseModel):
    created_by_id: str

    default: bool

    guid: str

    name: Optional[str] = None

    nickname: str

    url: Optional[str] = None

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


ProviderListResponse = List[ProviderListResponseItem]
