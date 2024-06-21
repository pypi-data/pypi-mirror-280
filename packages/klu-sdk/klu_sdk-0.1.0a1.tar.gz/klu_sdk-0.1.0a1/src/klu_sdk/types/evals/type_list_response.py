# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["TypeListResponse", "TypeListResponseItem"]


class TypeListResponseItem(BaseModel):
    eval_function: Optional[str] = None

    eval_run_type: str

    guid: str

    name: str

    owner: str

    type: str

    created_at: Optional[object] = None

    metadata: Optional[object] = None

    updated_at: Optional[object] = None


TypeListResponse = List[TypeListResponseItem]
