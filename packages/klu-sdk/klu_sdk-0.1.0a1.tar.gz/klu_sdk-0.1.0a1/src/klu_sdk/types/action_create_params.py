# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required, Annotated

from typing import Union, Iterable, Optional, List

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = [
    "ActionCreateParams",
    "PromptUnionMember1",
    "PromptUnionMember1ContentUnionMember1",
    "PromptUnionMember1ContentUnionMember1UnionMember0",
    "PromptUnionMember1ContentUnionMember1UnionMember1",
    "PromptUnionMember1ContentUnionMember1UnionMember1ImageURL",
    "PromptUnionMember1ToolCall",
    "PromptUnionMember1ToolCallFunction",
    "ModelConfig",
    "ModelConfigLogitBia",
]


class ActionCreateParams(TypedDict, total=False):
    action_type: Required[Literal["prompt", "chat"]]

    app: Required[str]

    description: Required[str]

    model: Required[str]

    name: Required[str]

    prompt: Required[Union[str, Iterable[PromptUnionMember1]]]

    model_config: ModelConfig

    system_message: str


class PromptUnionMember1ContentUnionMember1UnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class PromptUnionMember1ContentUnionMember1UnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]


class PromptUnionMember1ContentUnionMember1UnionMember1(TypedDict, total=False):
    image_url: Required[PromptUnionMember1ContentUnionMember1UnionMember1ImageURL]

    type: Required[Literal["image_url"]]


PromptUnionMember1ContentUnionMember1 = Union[
    PromptUnionMember1ContentUnionMember1UnionMember0, PromptUnionMember1ContentUnionMember1UnionMember1
]


class PromptUnionMember1ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class PromptUnionMember1ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[PromptUnionMember1ToolCallFunction]

    type: Required[str]


class PromptUnionMember1(TypedDict, total=False):
    role: Required[str]

    content: Union[Optional[str], Iterable[PromptUnionMember1ContentUnionMember1], object]

    tool_call_id: str

    tool_calls: Iterable[PromptUnionMember1ToolCall]


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
