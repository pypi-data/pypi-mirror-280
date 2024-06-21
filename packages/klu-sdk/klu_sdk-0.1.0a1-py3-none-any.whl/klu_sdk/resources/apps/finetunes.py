# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.apps.finetune_list_response import FinetuneListResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.apps import finetune_list_params

__all__ = ["FinetunesResource", "AsyncFinetunesResource"]


class FinetunesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FinetunesResourceWithRawResponse:
        return FinetunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinetunesResourceWithStreamingResponse:
        return FinetunesResourceWithStreamingResponse(self)

    def list(
        self,
        guid: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        skip: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._get(
            f"/apps/{guid}/finetunes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    finetune_list_params.FinetuneListParams,
                ),
            ),
            cast_to=FinetuneListResponse,
        )


class AsyncFinetunesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFinetunesResourceWithRawResponse:
        return AsyncFinetunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinetunesResourceWithStreamingResponse:
        return AsyncFinetunesResourceWithStreamingResponse(self)

    async def list(
        self,
        guid: str,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        skip: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._get(
            f"/apps/{guid}/finetunes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "skip": skip,
                    },
                    finetune_list_params.FinetuneListParams,
                ),
            ),
            cast_to=FinetuneListResponse,
        )


class FinetunesResourceWithRawResponse:
    def __init__(self, finetunes: FinetunesResource) -> None:
        self._finetunes = finetunes

        self.list = to_raw_response_wrapper(
            finetunes.list,
        )


class AsyncFinetunesResourceWithRawResponse:
    def __init__(self, finetunes: AsyncFinetunesResource) -> None:
        self._finetunes = finetunes

        self.list = async_to_raw_response_wrapper(
            finetunes.list,
        )


class FinetunesResourceWithStreamingResponse:
    def __init__(self, finetunes: FinetunesResource) -> None:
        self._finetunes = finetunes

        self.list = to_streamed_response_wrapper(
            finetunes.list,
        )


class AsyncFinetunesResourceWithStreamingResponse:
    def __init__(self, finetunes: AsyncFinetunesResource) -> None:
        self._finetunes = finetunes

        self.list = async_to_streamed_response_wrapper(
            finetunes.list,
        )
