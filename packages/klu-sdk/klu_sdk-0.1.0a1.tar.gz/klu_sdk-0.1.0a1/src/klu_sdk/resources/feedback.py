# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.feedback_create_response import FeedbackCreateResponse

from .._utils import maybe_transform, async_maybe_transform

from typing import Dict

from ..types.feedback_retrieve_response import FeedbackRetrieveResponse

from ..types.feedback_update_response import FeedbackUpdateResponse

from ..types.feedback_list_response import FeedbackListResponse

from ..types.feedback_delete_response import FeedbackDeleteResponse

from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import SyncAPIClient, AsyncAPIClient, _merge_mappings, AsyncPaginator, make_request_options, HttpxBinaryResponseContent
from ..types import shared_params
from ..types import feedback_create_params
from ..types import feedback_update_params
from ..types import feedback_list_params

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]

class FeedbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self)

    def create(self,
    *,
    data: str,
    source: str,
    type: str,
    value: str,
    created_by_id: str | NotGiven = NOT_GIVEN,
    created_by_id: str | NotGiven = NOT_GIVEN,
    metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/feedback",
            body=maybe_transform({
                "data": data,
                "source": source,
                "type": type,
                "value": value,
                "created_by_id": created_by_id,
                "metadata": metadata,
            }, feedback_create_params.FeedbackCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackCreateResponse,
        )

    def retrieve(self,
    guid: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
          raise ValueError(
            f'Expected a non-empty value for `guid` but received {guid!r}'
          )
        return self._get(
            f"/feedback/{guid}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackRetrieveResponse,
        )

    def update(self,
    guid: str,
    *,
    created_by_id: str,
    data: str,
    metadata: Dict[str, object],
    source: str,
    type: str,
    value: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
          raise ValueError(
            f'Expected a non-empty value for `guid` but received {guid!r}'
          )
        return self._put(
            f"/feedback/{guid}",
            body=maybe_transform({
                "created_by_id": created_by_id,
                "data": data,
                "metadata": metadata,
                "source": source,
                "type": type,
                "value": value,
            }, feedback_update_params.FeedbackUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackUpdateResponse,
        )

    def list(self,
    *,
    limit: float | NotGiven = NOT_GIVEN,
    skip: float | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/feedback",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "limit": limit,
                "skip": skip,
            }, feedback_list_params.FeedbackListParams)),
            cast_to=FeedbackListResponse,
        )

    def delete(self,
    guid: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
          raise ValueError(
            f'Expected a non-empty value for `guid` but received {guid!r}'
          )
        return self._delete(
            f"/feedback/{guid}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackDeleteResponse,
        )

class AsyncFeedbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def create(self,
    *,
    data: str,
    source: str,
    type: str,
    value: str,
    created_by_id: str | NotGiven = NOT_GIVEN,
    created_by_id: str | NotGiven = NOT_GIVEN,
    metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/feedback",
            body=await async_maybe_transform({
                "data": data,
                "source": source,
                "type": type,
                "value": value,
                "created_by_id": created_by_id,
                "metadata": metadata,
            }, feedback_create_params.FeedbackCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackCreateResponse,
        )

    async def retrieve(self,
    guid: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
          raise ValueError(
            f'Expected a non-empty value for `guid` but received {guid!r}'
          )
        return await self._get(
            f"/feedback/{guid}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackRetrieveResponse,
        )

    async def update(self,
    guid: str,
    *,
    created_by_id: str,
    data: str,
    metadata: Dict[str, object],
    source: str,
    type: str,
    value: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
          raise ValueError(
            f'Expected a non-empty value for `guid` but received {guid!r}'
          )
        return await self._put(
            f"/feedback/{guid}",
            body=await async_maybe_transform({
                "created_by_id": created_by_id,
                "data": data,
                "metadata": metadata,
                "source": source,
                "type": type,
                "value": value,
            }, feedback_update_params.FeedbackUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackUpdateResponse,
        )

    async def list(self,
    *,
    limit: float | NotGiven = NOT_GIVEN,
    skip: float | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/feedback",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "limit": limit,
                "skip": skip,
            }, feedback_list_params.FeedbackListParams)),
            cast_to=FeedbackListResponse,
        )

    async def delete(self,
    guid: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> FeedbackDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
          raise ValueError(
            f'Expected a non-empty value for `guid` but received {guid!r}'
          )
        return await self._delete(
            f"/feedback/{guid}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedbackDeleteResponse,
        )

class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_raw_response_wrapper(
            feedback.create,
        )
        self.retrieve = to_raw_response_wrapper(
            feedback.retrieve,
        )
        self.update = to_raw_response_wrapper(
            feedback.update,
        )
        self.list = to_raw_response_wrapper(
            feedback.list,
        )
        self.delete = to_raw_response_wrapper(
            feedback.delete,
        )

class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_raw_response_wrapper(
            feedback.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            feedback.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            feedback.update,
        )
        self.list = async_to_raw_response_wrapper(
            feedback.list,
        )
        self.delete = async_to_raw_response_wrapper(
            feedback.delete,
        )

class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_streamed_response_wrapper(
            feedback.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            feedback.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            feedback.update,
        )
        self.list = to_streamed_response_wrapper(
            feedback.list,
        )
        self.delete = to_streamed_response_wrapper(
            feedback.delete,
        )

class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_streamed_response_wrapper(
            feedback.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            feedback.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            feedback.update,
        )
        self.list = async_to_streamed_response_wrapper(
            feedback.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            feedback.delete,
        )