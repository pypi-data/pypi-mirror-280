# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["WorkflowListResponse", "WorkflowListResponseItem"]


class WorkflowListResponseItem(BaseModel):
    created_by_id: str

    guid: str

    last_updated_by_id: Optional[str] = None

    name: Optional[str] = None

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


WorkflowListResponse = List[WorkflowListResponseItem]
