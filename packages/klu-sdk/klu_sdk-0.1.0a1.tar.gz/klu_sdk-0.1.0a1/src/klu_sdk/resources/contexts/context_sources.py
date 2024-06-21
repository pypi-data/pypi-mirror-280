# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.contexts.context_source_create_response import ContextSourceCreateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ...types.contexts.context_source_retrieve_response import ContextSourceRetrieveResponse

from ...types.contexts.context_source_update_response import ContextSourceUpdateResponse

from typing import Iterable

from ...types.contexts.context_source_list_response import ContextSourceListResponse

from ...types.contexts.context_source_delete_response import ContextSourceDeleteResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types.contexts import context_source_update_params

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
from ...types.contexts import context_source_create_params
from ...types.contexts import context_source_update_params

__all__ = ["ContextSourcesResource", "AsyncContextSourcesResource"]


class ContextSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContextSourcesResourceWithRawResponse:
        return ContextSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextSourcesResourceWithStreamingResponse:
        return ContextSourcesResourceWithStreamingResponse(self)

    def create(
        self,
        context_guid: str,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_guid:
            raise ValueError(f"Expected a non-empty value for `context_guid` but received {context_guid!r}")
        return self._post(
            f"/contexts/{context_guid}/context_sources",
            body=maybe_transform({"url": url}, context_source_create_params.ContextSourceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceCreateResponse,
        )

    def retrieve(
        self,
        guid: str,
        *,
        context_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_guid:
            raise ValueError(f"Expected a non-empty value for `context_guid` but received {context_guid!r}")
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._get(
            f"/contexts/{context_guid}/context_sources/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceRetrieveResponse,
        )

    def update(
        self,
        guid: str,
        *,
        context_guid: str,
        name: str,
        splitter_config: context_source_update_params.SplitterConfig,
        loader_config: Iterable[context_source_update_params.LoaderConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_guid:
            raise ValueError(f"Expected a non-empty value for `context_guid` but received {context_guid!r}")
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._put(
            f"/contexts/{context_guid}/context_sources/{guid}",
            body=maybe_transform(
                {
                    "name": name,
                    "splitter_config": splitter_config,
                    "loader_config": loader_config,
                },
                context_source_update_params.ContextSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceUpdateResponse,
        )

    def list(
        self,
        context: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context:
            raise ValueError(f"Expected a non-empty value for `context` but received {context!r}")
        return self._get(
            f"/contexts/{context}/context_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceListResponse,
        )

    def delete(
        self,
        guid: str,
        *,
        context: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context:
            raise ValueError(f"Expected a non-empty value for `context` but received {context!r}")
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._delete(
            f"/contexts/{context}/context_sources/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceDeleteResponse,
        )


class AsyncContextSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContextSourcesResourceWithRawResponse:
        return AsyncContextSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextSourcesResourceWithStreamingResponse:
        return AsyncContextSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        context_guid: str,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_guid:
            raise ValueError(f"Expected a non-empty value for `context_guid` but received {context_guid!r}")
        return await self._post(
            f"/contexts/{context_guid}/context_sources",
            body=await async_maybe_transform({"url": url}, context_source_create_params.ContextSourceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceCreateResponse,
        )

    async def retrieve(
        self,
        guid: str,
        *,
        context_guid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_guid:
            raise ValueError(f"Expected a non-empty value for `context_guid` but received {context_guid!r}")
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._get(
            f"/contexts/{context_guid}/context_sources/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceRetrieveResponse,
        )

    async def update(
        self,
        guid: str,
        *,
        context_guid: str,
        name: str,
        splitter_config: context_source_update_params.SplitterConfig,
        loader_config: Iterable[context_source_update_params.LoaderConfig] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context_guid:
            raise ValueError(f"Expected a non-empty value for `context_guid` but received {context_guid!r}")
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._put(
            f"/contexts/{context_guid}/context_sources/{guid}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "splitter_config": splitter_config,
                    "loader_config": loader_config,
                },
                context_source_update_params.ContextSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceUpdateResponse,
        )

    async def list(
        self,
        context: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context:
            raise ValueError(f"Expected a non-empty value for `context` but received {context!r}")
        return await self._get(
            f"/contexts/{context}/context_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceListResponse,
        )

    async def delete(
        self,
        guid: str,
        *,
        context: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextSourceDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not context:
            raise ValueError(f"Expected a non-empty value for `context` but received {context!r}")
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._delete(
            f"/contexts/{context}/context_sources/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextSourceDeleteResponse,
        )


class ContextSourcesResourceWithRawResponse:
    def __init__(self, context_sources: ContextSourcesResource) -> None:
        self._context_sources = context_sources

        self.create = to_raw_response_wrapper(
            context_sources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            context_sources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            context_sources.update,
        )
        self.list = to_raw_response_wrapper(
            context_sources.list,
        )
        self.delete = to_raw_response_wrapper(
            context_sources.delete,
        )


class AsyncContextSourcesResourceWithRawResponse:
    def __init__(self, context_sources: AsyncContextSourcesResource) -> None:
        self._context_sources = context_sources

        self.create = async_to_raw_response_wrapper(
            context_sources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            context_sources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            context_sources.update,
        )
        self.list = async_to_raw_response_wrapper(
            context_sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            context_sources.delete,
        )


class ContextSourcesResourceWithStreamingResponse:
    def __init__(self, context_sources: ContextSourcesResource) -> None:
        self._context_sources = context_sources

        self.create = to_streamed_response_wrapper(
            context_sources.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            context_sources.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            context_sources.update,
        )
        self.list = to_streamed_response_wrapper(
            context_sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            context_sources.delete,
        )


class AsyncContextSourcesResourceWithStreamingResponse:
    def __init__(self, context_sources: AsyncContextSourcesResource) -> None:
        self._context_sources = context_sources

        self.create = async_to_streamed_response_wrapper(
            context_sources.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            context_sources.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            context_sources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            context_sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            context_sources.delete,
        )
