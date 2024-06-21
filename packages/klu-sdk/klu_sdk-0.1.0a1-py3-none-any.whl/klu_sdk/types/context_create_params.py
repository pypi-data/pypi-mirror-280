# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ContextCreateParams", "SplitterConfig"]


class ContextCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    response_length: Annotated[float, PropertyInfo(alias="responseLength")]

    splitter_config: Annotated[SplitterConfig, PropertyInfo(alias="splitterConfig")]


class SplitterConfig(TypedDict, total=False):
    chunk_overlap: Annotated[float, PropertyInfo(alias="chunkOverlap")]

    chunk_size: Annotated[float, PropertyInfo(alias="chunkSize")]

    splitter: str
