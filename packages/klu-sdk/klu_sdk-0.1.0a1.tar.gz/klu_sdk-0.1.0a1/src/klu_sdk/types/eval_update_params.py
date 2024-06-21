# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable, Union, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["EvalUpdateParams", "EvalType", "EvalTypeMetadata", "EvalTypeMetadataVariable"]


class EvalUpdateParams(TypedDict, total=False):
    eval_types: Required[Iterable[EvalType]]

    action: str

    alert_on_fail: bool

    dataset: str

    name: str

    sampling_rate: float

    version: str


class EvalTypeMetadataVariable(TypedDict, total=False):
    name: Required[str]

    value: Required[Union[str, float, bool, Dict[str, object]]]


class EvalTypeMetadata(TypedDict, total=False):
    variables: Iterable[EvalTypeMetadataVariable]


class EvalType(TypedDict, total=False):
    guid: Required[str]

    metadata: EvalTypeMetadata

    name: str

    new_record: bool
