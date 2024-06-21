# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["ExperimentDeleteResponse"]


class ExperimentDeleteResponse(BaseModel):
    deleted: bool

    guid: str

    name: str

    primary_action: str

    secondary_action: str

    status: str

    created_at: Optional[object] = None

    updated_at: Optional[object] = None
