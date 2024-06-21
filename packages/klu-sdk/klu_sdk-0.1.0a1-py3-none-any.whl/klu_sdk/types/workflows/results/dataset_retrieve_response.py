# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....types import shared

__all__ = ["DatasetRetrieveResponse", "Block"]


class Block(BaseModel):
    guid: str

    name: Optional[str] = None

    output: str


class DatasetRetrieveResponse(BaseModel):
    blocks: List[Block]

    final: str
