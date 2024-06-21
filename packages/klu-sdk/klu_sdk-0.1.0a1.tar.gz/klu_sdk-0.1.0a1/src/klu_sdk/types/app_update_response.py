# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["AppUpdateResponse"]


class AppUpdateResponse(BaseModel):
    created_by_id: str

    description: Optional[str] = None

    guid: str

    last_updated_by_id: Optional[str] = None

    name: str

    created_at: Optional[object] = None

    updated_at: Optional[object] = None
