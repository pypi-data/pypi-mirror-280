# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["StudioChatResponse"]


class StudioChatResponse(BaseModel):
    data_guid: Optional[str] = None

    feedback_url: Optional[str] = None

    full_response: Optional[object] = None

    msg: Optional[object] = None

    result_url: Optional[str] = None

    streaming: Optional[bool] = None

    streaming_url: Optional[str] = None
