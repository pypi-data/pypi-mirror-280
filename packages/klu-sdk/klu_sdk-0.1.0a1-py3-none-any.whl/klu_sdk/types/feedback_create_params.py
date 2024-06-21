# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from .._utils import PropertyInfo

from typing import Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    data: Required[str]

    source: Required[str]

    type: Required[str]

    value: Required[str]

    created_by_id: str

    created_by_id: Annotated[str, PropertyInfo(alias="createdById")]

    metadata: Dict[str, object]
