# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["ContextSourceUpdateResponse"]


class ContextSourceUpdateResponse(BaseModel):
    created_by_id: Optional[str] = None

    guid: str

    indexing_status: Optional[str] = None

    loader_id: float

    name: str

    url: Optional[str] = None

    created_at: Optional[object] = None

    indexed_at: Optional[object] = None

    indexing_metadata: Optional[object] = None

    loader_config: Optional[object] = None

    splitter_config: Optional[object] = None

    updated_at: Optional[object] = None
