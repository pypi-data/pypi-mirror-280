# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["EvalDeleteResponse", "Dataset"]


class Dataset(BaseModel):
    created_by_id: str

    guid: str

    name: str

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


class EvalDeleteResponse(BaseModel):
    created_by_id: str

    guid: str

    name: str

    created_at: Optional[object] = None

    dataset: Optional[Dataset] = None

    metadata: Optional[object] = None

    updated_at: Optional[object] = None
