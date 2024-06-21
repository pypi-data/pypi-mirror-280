# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["DataUpdateParams"]


class DataUpdateParams(TypedDict, total=False):
    action: str

    app: str

    full_prompt_sent: str

    input: str

    latency: float

    metadata: object

    model: str

    model_provider: str

    num_input_tokens: float

    num_output_tokens: float

    output: str

    prompt_template: str

    raw_llm_request: Dict[str, object]

    raw_llm_response: str

    session: str

    system_message: str

    version_id: str
