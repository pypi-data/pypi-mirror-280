# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .context_sources import ContextSourcesResource, AsyncContextSourcesResource

from ..._compat import cached_property

from .documents import DocumentsResource, AsyncDocumentsResource

from ...types.context_create_response import ContextCreateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ...types.context_retrieve_response import ContextRetrieveResponse

from ...types.context_update_response import ContextUpdateResponse

from ...types.context_list_response import ContextListResponse

from ...types.context_delete_response import ContextDeleteResponse

from ...types.context_add_files_response import ContextAddFilesResponse

from typing import List

from ...types.context_embed_response import ContextEmbedResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types import context_create_params, context_update_params

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
from ...types import context_create_params
from ...types import context_update_params
from ...types import context_add_files_params
from .context_sources import (
    ContextSourcesResource,
    AsyncContextSourcesResource,
    ContextSourcesResourceWithRawResponse,
    AsyncContextSourcesResourceWithRawResponse,
    ContextSourcesResourceWithStreamingResponse,
    AsyncContextSourcesResourceWithStreamingResponse,
)
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)

__all__ = ["ContextsResource", "AsyncContextsResource"]


class ContextsResource(SyncAPIResource):
    @cached_property
    def context_sources(self) -> ContextSourcesResource:
        return ContextSourcesResource(self._client)

    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContextsResourceWithRawResponse:
        return ContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextsResourceWithStreamingResponse:
        return ContextsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        response_length: float | NotGiven = NOT_GIVEN,
        splitter_config: context_create_params.SplitterConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contexts",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "response_length": response_length,
                    "splitter_config": splitter_config,
                },
                context_create_params.ContextCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextCreateResponse,
        )

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
    ) -> ContextRetrieveResponse:
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
            f"/contexts/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextRetrieveResponse,
        )

    def update(
        self,
        guid: str,
        *,
        response_length: float,
        response_mode: str,
        similarity_top_k: float,
        description: str | NotGiven = NOT_GIVEN,
        loader_id: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rerank_llm_top_n: float | NotGiven = NOT_GIVEN,
        similarity_cutoff: float | NotGiven = NOT_GIVEN,
        splitter_config: context_update_params.SplitterConfig | NotGiven = NOT_GIVEN,
        type_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._put(
            f"/contexts/{guid}",
            body=maybe_transform(
                {
                    "response_length": response_length,
                    "response_mode": response_mode,
                    "similarity_top_k": similarity_top_k,
                    "description": description,
                    "loader_id": loader_id,
                    "name": name,
                    "rerank_llm_top_n": rerank_llm_top_n,
                    "similarity_cutoff": similarity_cutoff,
                    "splitter_config": splitter_config,
                    "type_id": type_id,
                },
                context_update_params.ContextUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextListResponse:
        return self._get(
            "/contexts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextListResponse,
        )

    def delete(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._delete(
            f"/contexts/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDeleteResponse,
        )

    def add_files(
        self,
        guid: str,
        *,
        files: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextAddFilesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._post(
            f"/contexts/{guid}/add_files",
            body=maybe_transform({"files": files}, context_add_files_params.ContextAddFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextAddFilesResponse,
        )

    def embed(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextEmbedResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return self._post(
            f"/contexts/{guid}/embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextEmbedResponse,
        )


class AsyncContextsResource(AsyncAPIResource):
    @cached_property
    def context_sources(self) -> AsyncContextSourcesResource:
        return AsyncContextSourcesResource(self._client)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContextsResourceWithRawResponse:
        return AsyncContextsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextsResourceWithStreamingResponse:
        return AsyncContextsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        response_length: float | NotGiven = NOT_GIVEN,
        splitter_config: context_create_params.SplitterConfig | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contexts",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "response_length": response_length,
                    "splitter_config": splitter_config,
                },
                context_create_params.ContextCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextCreateResponse,
        )

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
    ) -> ContextRetrieveResponse:
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
            f"/contexts/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextRetrieveResponse,
        )

    async def update(
        self,
        guid: str,
        *,
        response_length: float,
        response_mode: str,
        similarity_top_k: float,
        description: str | NotGiven = NOT_GIVEN,
        loader_id: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rerank_llm_top_n: float | NotGiven = NOT_GIVEN,
        similarity_cutoff: float | NotGiven = NOT_GIVEN,
        splitter_config: context_update_params.SplitterConfig | NotGiven = NOT_GIVEN,
        type_id: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextUpdateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._put(
            f"/contexts/{guid}",
            body=await async_maybe_transform(
                {
                    "response_length": response_length,
                    "response_mode": response_mode,
                    "similarity_top_k": similarity_top_k,
                    "description": description,
                    "loader_id": loader_id,
                    "name": name,
                    "rerank_llm_top_n": rerank_llm_top_n,
                    "similarity_cutoff": similarity_cutoff,
                    "splitter_config": splitter_config,
                    "type_id": type_id,
                },
                context_update_params.ContextUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextListResponse:
        return await self._get(
            "/contexts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextListResponse,
        )

    async def delete(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextDeleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._delete(
            f"/contexts/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDeleteResponse,
        )

    async def add_files(
        self,
        guid: str,
        *,
        files: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextAddFilesResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._post(
            f"/contexts/{guid}/add_files",
            body=await async_maybe_transform({"files": files}, context_add_files_params.ContextAddFilesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextAddFilesResponse,
        )

    async def embed(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContextEmbedResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guid:
            raise ValueError(f"Expected a non-empty value for `guid` but received {guid!r}")
        return await self._post(
            f"/contexts/{guid}/embed",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextEmbedResponse,
        )


class ContextsResourceWithRawResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contexts.update,
        )
        self.list = to_raw_response_wrapper(
            contexts.list,
        )
        self.delete = to_raw_response_wrapper(
            contexts.delete,
        )
        self.add_files = to_raw_response_wrapper(
            contexts.add_files,
        )
        self.embed = to_raw_response_wrapper(
            contexts.embed,
        )

    @cached_property
    def context_sources(self) -> ContextSourcesResourceWithRawResponse:
        return ContextSourcesResourceWithRawResponse(self._contexts.context_sources)

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._contexts.documents)


class AsyncContextsResourceWithRawResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_raw_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contexts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contexts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contexts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contexts.delete,
        )
        self.add_files = async_to_raw_response_wrapper(
            contexts.add_files,
        )
        self.embed = async_to_raw_response_wrapper(
            contexts.embed,
        )

    @cached_property
    def context_sources(self) -> AsyncContextSourcesResourceWithRawResponse:
        return AsyncContextSourcesResourceWithRawResponse(self._contexts.context_sources)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._contexts.documents)


class ContextsResourceWithStreamingResponse:
    def __init__(self, contexts: ContextsResource) -> None:
        self._contexts = contexts

        self.create = to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contexts.update,
        )
        self.list = to_streamed_response_wrapper(
            contexts.list,
        )
        self.delete = to_streamed_response_wrapper(
            contexts.delete,
        )
        self.add_files = to_streamed_response_wrapper(
            contexts.add_files,
        )
        self.embed = to_streamed_response_wrapper(
            contexts.embed,
        )

    @cached_property
    def context_sources(self) -> ContextSourcesResourceWithStreamingResponse:
        return ContextSourcesResourceWithStreamingResponse(self._contexts.context_sources)

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._contexts.documents)


class AsyncContextsResourceWithStreamingResponse:
    def __init__(self, contexts: AsyncContextsResource) -> None:
        self._contexts = contexts

        self.create = async_to_streamed_response_wrapper(
            contexts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contexts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contexts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contexts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contexts.delete,
        )
        self.add_files = async_to_streamed_response_wrapper(
            contexts.add_files,
        )
        self.embed = async_to_streamed_response_wrapper(
            contexts.embed,
        )

    @cached_property
    def context_sources(self) -> AsyncContextSourcesResourceWithStreamingResponse:
        return AsyncContextSourcesResourceWithStreamingResponse(self._contexts.context_sources)

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._contexts.documents)
