# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...types import shared

__all__ = ["UsageRetrieveResponse", "UsageRetrieveResponseItem"]


class UsageRetrieveResponseItem(BaseModel):
    feature: str

    limit: float

    used: float


UsageRetrieveResponse = List[UsageRetrieveResponseItem]
