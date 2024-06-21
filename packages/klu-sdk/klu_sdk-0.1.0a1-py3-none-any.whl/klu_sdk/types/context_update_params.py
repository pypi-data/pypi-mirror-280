# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ContextUpdateParams", "SplitterConfig"]


class ContextUpdateParams(TypedDict, total=False):
    response_length: Required[Annotated[float, PropertyInfo(alias="responseLength")]]

    response_mode: Required[Annotated[str, PropertyInfo(alias="responseMode")]]

    similarity_top_k: Required[Annotated[float, PropertyInfo(alias="similarityTopK")]]

    description: str

    loader_id: Annotated[float, PropertyInfo(alias="loaderId")]

    name: str

    rerank_llm_top_n: Annotated[float, PropertyInfo(alias="rerankLlmTopN")]

    similarity_cutoff: Annotated[float, PropertyInfo(alias="similarityCutoff")]

    splitter_config: Annotated[SplitterConfig, PropertyInfo(alias="splitterConfig")]

    type_id: Annotated[float, PropertyInfo(alias="typeId")]


class SplitterConfig(TypedDict, total=False):
    chunk_overlap: Required[Annotated[float, PropertyInfo(alias="chunkOverlap")]]

    chunk_size: Required[Annotated[float, PropertyInfo(alias="chunkSize")]]

    code_language: str

    separator: str

    splitter: str
