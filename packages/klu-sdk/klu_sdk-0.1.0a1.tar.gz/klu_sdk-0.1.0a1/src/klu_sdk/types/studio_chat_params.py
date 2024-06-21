# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Optional, Iterable, Dict, List

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["StudioChatParams", "Message", "ModelConfig", "ModelConfigLogitBia", "TemplateMessage"]


class StudioChatParams(TypedDict, total=False):
    messages: Required[Optional[Iterable[Message]]]

    model_config: Required[Annotated[ModelConfig, PropertyInfo(alias="modelConfig")]]

    model_guid: Required[Annotated[str, PropertyInfo(alias="modelGuid")]]

    template_messages: Required[Annotated[Iterable[TemplateMessage], PropertyInfo(alias="templateMessages")]]

    user: Required[Optional[str]]

    values: Required[Optional[Dict[str, object]]]

    action_guid: Annotated[Optional[str], PropertyInfo(alias="actionGuid")]

    index_guids: Annotated[Optional[List[str]], PropertyInfo(alias="indexGuids")]

    output_format: Annotated[Optional[str], PropertyInfo(alias="outputFormat")]

    output_instructions: Annotated[Optional[str], PropertyInfo(alias="outputInstructions")]

    persist: bool

    session: Optional[str]

    streaming: bool

    tool_guids: Annotated[Optional[List[str]], PropertyInfo(alias="toolGuids")]

    version: Optional[float]


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]

    files: Optional[List[str]]


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


class TemplateMessage(TypedDict, total=False):
    content: Required[str]

    role: Required[str]

    files: Optional[List[str]]
