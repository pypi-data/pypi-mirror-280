# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Dict, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["RunListResponse", "RunListResponseItem", "RunListResponseItemMetadata"]


class RunListResponseItemMetadata(BaseModel):
    average_cost: str

    average_latency: str

    run_items_completed: float

    scores: Dict[str, str]

    status: str

    total_cost: str

    total_latency: str

    total_run_items: float

    execution_time: Optional[object] = None

    execution_time_per_item: Optional[object] = None


class RunListResponseItem(BaseModel):
    action: str

    created_by_id: str

    deleted: bool

    eval: str

    guid: str

    metadata: RunListResponseItemMetadata

    run_number: float

    version: str

    created_at: Optional[object] = None

    updated_at: Optional[object] = None


RunListResponse = List[RunListResponseItem]
