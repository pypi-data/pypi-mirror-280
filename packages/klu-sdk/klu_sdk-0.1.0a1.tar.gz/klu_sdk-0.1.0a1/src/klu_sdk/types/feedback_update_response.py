# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["FeedbackUpdateResponse"]


class FeedbackUpdateResponse(BaseModel):
    created_by_id: str

    data: str

    deleted: bool

    guid: str

    source: str

    type: str

    value: str

    created_at: Optional[object] = None

    metadata: Optional[object] = None

    updated_at: Optional[object] = None
