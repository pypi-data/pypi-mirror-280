# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from ..._utils import PropertyInfo

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ContextSourceUpdateParams", "SplitterConfig", "LoaderConfig"]


class ContextSourceUpdateParams(TypedDict, total=False):
    context_guid: Required[Annotated[str, PropertyInfo(alias="contextGuid")]]

    name: Required[str]

    splitter_config: Required[Annotated[SplitterConfig, PropertyInfo(alias="splitterConfig")]]

    loader_config: Annotated[Iterable[LoaderConfig], PropertyInfo(alias="loaderConfig")]


class SplitterConfig(TypedDict, total=False):
    code_language: str

    separator: str

    splitter: str


class LoaderConfig(TypedDict, total=False):
    name: Required[str]

    value: Required[str]

    required: bool
