# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.actions.result_retrieve_response import ResultRetrieveResponse

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

__all__ = ["ResultResource", "AsyncResultResource"]


class ResultResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultResourceWithRawResponse:
        return ResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultResourceWithStreamingResponse:
        return ResultResourceWithStreamingResponse(self)

    def retrieve(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultRetrieveResponse:
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
            f"/actions/result/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrieveResponse,
        )


class AsyncResultResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultResourceWithRawResponse:
        return AsyncResultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultResourceWithStreamingResponse:
        return AsyncResultResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultRetrieveResponse:
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
            f"/actions/result/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrieveResponse,
        )


class ResultResourceWithRawResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.retrieve = to_raw_response_wrapper(
            result.retrieve,
        )


class AsyncResultResourceWithRawResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.retrieve = async_to_raw_response_wrapper(
            result.retrieve,
        )


class ResultResourceWithStreamingResponse:
    def __init__(self, result: ResultResource) -> None:
        self._result = result

        self.retrieve = to_streamed_response_wrapper(
            result.retrieve,
        )


class AsyncResultResourceWithStreamingResponse:
    def __init__(self, result: AsyncResultResource) -> None:
        self._result = result

        self.retrieve = async_to_streamed_response_wrapper(
            result.retrieve,
        )
