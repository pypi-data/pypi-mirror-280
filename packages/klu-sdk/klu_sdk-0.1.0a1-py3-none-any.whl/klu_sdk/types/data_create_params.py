# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["DataCreateParams"]


class DataCreateParams(TypedDict, total=False):
    action: Required[str]

    input: Required[str]

    output: Required[str]

    full_prompt_sent: str

    latency: float

    metadata: Dict[str, object]

    model: str

    model_provider: str

    num_input_tokens: float

    num_output_tokens: float

    raw_llm_request: Dict[str, object]

    raw_llm_response: str

    session: str

    system_message: str
