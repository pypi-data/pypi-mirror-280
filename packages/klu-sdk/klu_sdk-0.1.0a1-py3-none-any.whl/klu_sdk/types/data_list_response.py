# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, Dict, Union, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["DataListResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    full_prompt_sent: str

    guid: str

    input: str

    latency: float

    model: str

    api_model_provider: str = FieldInfo(alias="model_provider")

    num_input_tokens: float

    num_output_tokens: float

    output: str

    updated_at: datetime

    metadata: Optional[Dict[str, Union[object, object]]] = None

    raw_llm_request: Optional[object] = None

    raw_llm_response: Optional[object] = None

    system_message: Optional[str] = None


class DataListResponse(BaseModel):
    data: List[Data]

    has_next_page: bool

    total_count: float
