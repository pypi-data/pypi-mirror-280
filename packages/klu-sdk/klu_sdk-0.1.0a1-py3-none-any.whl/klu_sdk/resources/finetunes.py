# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.finetune_create_response import FinetuneCreateResponse

from .._utils import maybe_transform, async_maybe_transform

from typing import Iterable

from ..types.finetune_retrieve_response import FinetuneRetrieveResponse

from ..types.finetune_update_response import FinetuneUpdateResponse

from ..types.finetune_list_response import FinetuneListResponse

from ..types.finetune_delete_response import FinetuneDeleteResponse

from ..types.finetune_status_response import FinetuneStatusResponse

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import finetune_create_params
from ..types import finetune_update_params
from ..types import finetune_list_params

__all__ = ["FinetunesResource", "AsyncFinetunesResource"]


class FinetunesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FinetunesResourceWithRawResponse:
        return FinetunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinetunesResourceWithStreamingResponse:
        return FinetunesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        app: str,
        base_model: str,
        data_ids: Iterable[float],
        dataset: str,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/finetune",
            body=maybe_transform(
                {
                    "app": app,
                    "base_model": base_model,
                    "data_ids": data_ids,
                    "dataset": dataset,
                    "name": name,
                    "metadata": metadata,
                },
                finetune_create_params.FinetuneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneCreateResponse,
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
    ) -> FinetuneRetrieveResponse:
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
            f"/finetune/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneRetrieveResponse,
        )

    def update(
        self,
        guid: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneUpdateResponse:
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
            f"/finetune/{guid}",
            body=maybe_transform({"name": name}, finetune_update_params.FinetuneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneUpdateResponse,
        )

    def list(
        self,
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
        return self._get(
            "/finetune",
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
    ) -> FinetuneDeleteResponse:
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
            f"/finetune/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneDeleteResponse,
        )

    def status(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneStatusResponse:
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
            f"/finetune/{guid}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneStatusResponse,
        )


class AsyncFinetunesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFinetunesResourceWithRawResponse:
        return AsyncFinetunesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinetunesResourceWithStreamingResponse:
        return AsyncFinetunesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        app: str,
        base_model: str,
        data_ids: Iterable[float],
        dataset: str,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/finetune",
            body=await async_maybe_transform(
                {
                    "app": app,
                    "base_model": base_model,
                    "data_ids": data_ids,
                    "dataset": dataset,
                    "name": name,
                    "metadata": metadata,
                },
                finetune_create_params.FinetuneCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneCreateResponse,
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
    ) -> FinetuneRetrieveResponse:
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
            f"/finetune/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneRetrieveResponse,
        )

    async def update(
        self,
        guid: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneUpdateResponse:
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
            f"/finetune/{guid}",
            body=await async_maybe_transform({"name": name}, finetune_update_params.FinetuneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneUpdateResponse,
        )

    async def list(
        self,
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
        return await self._get(
            "/finetune",
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
    ) -> FinetuneDeleteResponse:
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
            f"/finetune/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneDeleteResponse,
        )

    async def status(
        self,
        guid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinetuneStatusResponse:
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
            f"/finetune/{guid}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinetuneStatusResponse,
        )


class FinetunesResourceWithRawResponse:
    def __init__(self, finetunes: FinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = to_raw_response_wrapper(
            finetunes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            finetunes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            finetunes.update,
        )
        self.list = to_raw_response_wrapper(
            finetunes.list,
        )
        self.delete = to_raw_response_wrapper(
            finetunes.delete,
        )
        self.status = to_raw_response_wrapper(
            finetunes.status,
        )


class AsyncFinetunesResourceWithRawResponse:
    def __init__(self, finetunes: AsyncFinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = async_to_raw_response_wrapper(
            finetunes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            finetunes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            finetunes.update,
        )
        self.list = async_to_raw_response_wrapper(
            finetunes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            finetunes.delete,
        )
        self.status = async_to_raw_response_wrapper(
            finetunes.status,
        )


class FinetunesResourceWithStreamingResponse:
    def __init__(self, finetunes: FinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = to_streamed_response_wrapper(
            finetunes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            finetunes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            finetunes.update,
        )
        self.list = to_streamed_response_wrapper(
            finetunes.list,
        )
        self.delete = to_streamed_response_wrapper(
            finetunes.delete,
        )
        self.status = to_streamed_response_wrapper(
            finetunes.status,
        )


class AsyncFinetunesResourceWithStreamingResponse:
    def __init__(self, finetunes: AsyncFinetunesResource) -> None:
        self._finetunes = finetunes

        self.create = async_to_streamed_response_wrapper(
            finetunes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            finetunes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            finetunes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            finetunes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            finetunes.delete,
        )
        self.status = async_to_streamed_response_wrapper(
            finetunes.status,
        )
