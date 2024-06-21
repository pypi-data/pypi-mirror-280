# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import Optional, Iterable, List

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ActionUpdateParams", "ModelConfig", "ModelConfigLogitBia"]


class ActionUpdateParams(TypedDict, total=False):
    model_config: Required[ModelConfig]

    action_type: Literal["legacy", "prompt", "chat", "workflow", "worker"]

    app: str

    description: str

    model: str

    name: str

    prompt: str

    system_message: str


class ModelConfigLogitBia(TypedDict, total=False):
    bias_value: Required[Annotated[float, PropertyInfo(alias="biasValue")]]

    token_id: Required[Annotated[str, PropertyInfo(alias="tokenId")]]


class ModelConfig(TypedDict, total=False):
    frequency_penalty: Required[Annotated[float, PropertyInfo(alias="frequencyPenalty")]]

    max_response_length: Required[Annotated[float, PropertyInfo(alias="maxResponseLength")]]

    num_retries: Required[Annotated[float, PropertyInfo(alias="numRetries")]]

    presence_penalty: Required[Annotated[float, PropertyInfo(alias="presencePenalty")]]

    response_format: Required[Annotated[Optional[Literal["json"]], PropertyInfo(alias="responseFormat")]]

    seed: Required[Optional[float]]

    temperature: Required[float]

    timeout: Required[float]

    top_p: Required[Annotated[float, PropertyInfo(alias="topP")]]

    logit_bias: Annotated[Optional[Iterable[ModelConfigLogitBia]], PropertyInfo(alias="logitBias")]

    stop_sequence: Annotated[Optional[List[str]], PropertyInfo(alias="stopSequence")]
