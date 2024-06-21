# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Union, List, Dict

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = [
    "ActionGatewayPayloadResponse",
    "Headers",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1UnionMember0",
    "MessageContentUnionMember1UnionMember1",
    "MessageContentUnionMember1UnionMember1ImageURL",
    "MessageToolCall",
    "MessageToolCallFunction",
    "ResponseFormat",
]


class Headers(BaseModel):
    authorization: str = FieldInfo(alias="Authorization")

    x_klu_action_guid: Optional[str] = FieldInfo(alias="x-klu-action-guid", default=None)

    x_klu_api_key: Optional[str] = FieldInfo(alias="x-klu-api-key", default=None)


class MessageContentUnionMember1UnionMember0(BaseModel):
    text: str

    type: Literal["text"]


class MessageContentUnionMember1UnionMember1ImageURL(BaseModel):
    url: str


class MessageContentUnionMember1UnionMember1(BaseModel):
    image_url: MessageContentUnionMember1UnionMember1ImageURL

    type: Literal["image_url"]


MessageContentUnionMember1 = Union[MessageContentUnionMember1UnionMember0, MessageContentUnionMember1UnionMember1]


class MessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class MessageToolCall(BaseModel):
    id: str

    function: MessageToolCallFunction

    type: str


class Message(BaseModel):
    role: str

    content: Union[Optional[str], List[MessageContentUnionMember1], object, None] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[MessageToolCall]] = None


class ResponseFormat(BaseModel):
    type: Union[Literal["json_object"], Literal["text"], object, None] = None


class ActionGatewayPayloadResponse(BaseModel):
    headers: Headers

    messages: List[Message]

    model: str

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, float]] = None

    max_tokens: Optional[float] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[ResponseFormat] = None

    stop: Union[List[str], str, None] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None
