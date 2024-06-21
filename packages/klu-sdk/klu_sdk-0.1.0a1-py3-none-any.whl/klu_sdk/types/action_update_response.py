# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["ActionUpdateResponse"]


class ActionUpdateResponse(BaseModel):
    action_type: str

    app: str

    created_by_id: str

    description: Optional[str] = None

    guid: str

    model: str

    name: str

    prompt: Optional[str] = None

    status: str

    system_message: Optional[str] = None

    created_at: Optional[object] = None

    api_model_config: Optional[object] = FieldInfo(alias="model_config", default=None)

    updated_at: Optional[object] = None
