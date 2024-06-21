# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["ContextRetrieveResponse", "ContextRetrieveResponseItem"]


class ContextRetrieveResponseItem(BaseModel):
    created_by_id: str

    description: str

    guid: str

    name: str

    processed: bool

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


ContextRetrieveResponse = List[ContextRetrieveResponseItem]
