# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Union, Dict, Optional, Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = [
    "ActionGatewayPayloadParams",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1UnionMember0",
    "MessageContentUnionMember1UnionMember1",
    "MessageContentUnionMember1UnionMember1ImageURL",
    "MessageToolCall",
    "MessageToolCallFunction",
]


class ActionGatewayPayloadParams(TypedDict, total=False):
    input: Required[Union[Dict[str, object], str]]

    environment: str

    filter: str

    messages: Optional[Iterable[Message]]

    metadata_filter: Dict[str, object]

    version: float


class MessageContentUnionMember1UnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class MessageContentUnionMember1UnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]


class MessageContentUnionMember1UnionMember1(TypedDict, total=False):
    image_url: Required[MessageContentUnionMember1UnionMember1ImageURL]

    type: Required[Literal["image_url"]]


MessageContentUnionMember1 = Union[MessageContentUnionMember1UnionMember0, MessageContentUnionMember1UnionMember1]


class MessageToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[MessageToolCallFunction]

    type: Required[str]


class Message(TypedDict, total=False):
    role: Required[str]

    content: Union[Optional[str], Iterable[MessageContentUnionMember1], object]

    tool_call_id: str

    tool_calls: Iterable[MessageToolCall]
