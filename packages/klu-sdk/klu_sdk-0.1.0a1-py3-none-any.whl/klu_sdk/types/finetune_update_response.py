# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["FinetuneUpdateResponse"]


class FinetuneUpdateResponse(BaseModel):
    app: str

    created_by_id: str

    finetuned_model: Optional[str] = None

    guid: str

    name: str

    created_at: Optional[object] = None

    dataset: Optional[str] = None

    metadata: Optional[object] = None

    updated_at: Optional[object] = None
