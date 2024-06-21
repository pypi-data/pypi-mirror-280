# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from .._utils import PropertyInfo

from typing import Optional, Union, Dict, List, Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["StudioPromptParams", "ModelConfig", "ModelConfigLogitBia"]


class StudioPromptParams(TypedDict, total=False):
    model_config: Required[Annotated[ModelConfig, PropertyInfo(alias="modelConfig")]]

    model_guid: Required[Annotated[str, PropertyInfo(alias="modelGuid")]]

    prompt: Required[str]

    system_message: Required[Annotated[Optional[str], PropertyInfo(alias="systemMessage")]]

    user: Required[Optional[str]]

    values: Required[Union[Dict[str, object], str, None]]

    action_guid: Annotated[Optional[str], PropertyInfo(alias="actionGuid")]

    files: Optional[List[str]]

    index_guids: Annotated[Optional[List[str]], PropertyInfo(alias="indexGuids")]

    output_format: Annotated[Optional[str], PropertyInfo(alias="outputFormat")]

    output_instructions: Annotated[Optional[str], PropertyInfo(alias="outputInstructions")]

    persist: bool

    streaming: bool

    tool_guids: Annotated[Optional[List[str]], PropertyInfo(alias="toolGuids")]

    version: Optional[float]


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
