# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Union, Iterable, Dict, Optional

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = [
    "ActionPromptParams",
    "InputUnionMember0",
    "InputUnionMember0ContentUnionMember1",
    "InputUnionMember0ContentUnionMember1UnionMember0",
    "InputUnionMember0ContentUnionMember1UnionMember1",
    "InputUnionMember0ContentUnionMember1UnionMember1ImageURL",
    "InputUnionMember0ToolCall",
    "InputUnionMember0ToolCallFunction",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1UnionMember0",
    "MessageContentUnionMember1UnionMember1",
    "MessageContentUnionMember1UnionMember1ImageURL",
    "MessageToolCall",
    "MessageToolCallFunction",
]


class ActionPromptParams(TypedDict, total=False):
    input: Required[Union[Iterable[InputUnionMember0], Dict[str, object], str]]

    async_mode: bool

    cache: bool

    environment: str

    experiment: str

    ext_user_id: Annotated[str, PropertyInfo(alias="extUserId")]

    filter: str

    messages: Optional[Iterable[Message]]

    metadata: Dict[str, object]

    session: str

    streaming: bool

    version: float


class InputUnionMember0ContentUnionMember1UnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class InputUnionMember0ContentUnionMember1UnionMember1ImageURL(TypedDict, total=False):
    url: Required[str]


class InputUnionMember0ContentUnionMember1UnionMember1(TypedDict, total=False):
    image_url: Required[InputUnionMember0ContentUnionMember1UnionMember1ImageURL]

    type: Required[Literal["image_url"]]


InputUnionMember0ContentUnionMember1 = Union[
    InputUnionMember0ContentUnionMember1UnionMember0, InputUnionMember0ContentUnionMember1UnionMember1
]


class InputUnionMember0ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class InputUnionMember0ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[InputUnionMember0ToolCallFunction]

    type: Required[str]


class InputUnionMember0(TypedDict, total=False):
    role: Required[str]

    content: Union[Optional[str], Iterable[InputUnionMember0ContentUnionMember1], object]

    tool_call_id: str

    tool_calls: Iterable[InputUnionMember0ToolCall]


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
