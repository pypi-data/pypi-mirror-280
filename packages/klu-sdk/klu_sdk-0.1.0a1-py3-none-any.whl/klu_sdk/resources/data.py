# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.data_create_response import DataCreateResponse

from .._utils import maybe_transform, async_maybe_transform

from typing import Dict

from ..types.data_retrieve_response import DataRetrieveResponse

from ..types.data_update_response import DataUpdateResponse

from ..types.data_list_response import DataListResponse

from ..types.data_delete_response import DataDeleteResponse

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
from ..types import data_create_params
from ..types import data_update_params
from ..types import data_list_params

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        return DataResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action: str,
        input: str,
        output: str,
        full_prompt_sent: str | NotGiven = NOT_GIVEN,
        latency: float | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        model_provider: str | NotGiven = NOT_GIVEN,
        num_input_tokens: float | NotGiven = NOT_GIVEN,
        num_output_tokens: float | NotGiven = NOT_GIVEN,
        raw_llm_request: Dict[str, object] | NotGiven = NOT_GIVEN,
        raw_llm_response: str | NotGiven = NOT_GIVEN,
        session: str | NotGiven = NOT_GIVEN,
        system_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/data",
            body=maybe_transform(
                {
                    "action": action,
                    "input": input,
                    "output": output,
                    "full_prompt_sent": full_prompt_sent,
                    "latency": latency,
                    "metadata": metadata,
                    "model": model,
                    "model_provider": model_provider,
                    "num_input_tokens": num_input_tokens,
                    "num_output_tokens": num_output_tokens,
                    "raw_llm_request": raw_llm_request,
                    "raw_llm_response": raw_llm_response,
                    "session": session,
                    "system_message": system_message,
                },
                data_create_params.DataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataCreateResponse,
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
    ) -> DataRetrieveResponse:
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
            f"/data/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataRetrieveResponse,
        )

    def update(
        self,
        guid: str,
        *,
        action: str | NotGiven = NOT_GIVEN,
        app: str | NotGiven = NOT_GIVEN,
        full_prompt_sent: str | NotGiven = NOT_GIVEN,
        input: str | NotGiven = NOT_GIVEN,
        latency: float | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        model_provider: str | NotGiven = NOT_GIVEN,
        num_input_tokens: float | NotGiven = NOT_GIVEN,
        num_output_tokens: float | NotGiven = NOT_GIVEN,
        output: str | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        raw_llm_request: Dict[str, object] | NotGiven = NOT_GIVEN,
        raw_llm_response: str | NotGiven = NOT_GIVEN,
        session: str | NotGiven = NOT_GIVEN,
        system_message: str | NotGiven = NOT_GIVEN,
        version_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataUpdateResponse:
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
            f"/data/{guid}",
            body=maybe_transform(
                {
                    "action": action,
                    "app": app,
                    "full_prompt_sent": full_prompt_sent,
                    "input": input,
                    "latency": latency,
                    "metadata": metadata,
                    "model": model,
                    "model_provider": model_provider,
                    "num_input_tokens": num_input_tokens,
                    "num_output_tokens": num_output_tokens,
                    "output": output,
                    "prompt_template": prompt_template,
                    "raw_llm_request": raw_llm_request,
                    "raw_llm_response": raw_llm_response,
                    "session": session,
                    "system_message": system_message,
                    "version_id": version_id,
                },
                data_update_params.DataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataUpdateResponse,
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
    ) -> DataListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/data",
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
                    data_list_params.DataListParams,
                ),
            ),
            cast_to=DataListResponse,
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
    ) -> DataDeleteResponse:
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
            f"/data/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataDeleteResponse,
        )


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        return AsyncDataResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action: str,
        input: str,
        output: str,
        full_prompt_sent: str | NotGiven = NOT_GIVEN,
        latency: float | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        model_provider: str | NotGiven = NOT_GIVEN,
        num_input_tokens: float | NotGiven = NOT_GIVEN,
        num_output_tokens: float | NotGiven = NOT_GIVEN,
        raw_llm_request: Dict[str, object] | NotGiven = NOT_GIVEN,
        raw_llm_response: str | NotGiven = NOT_GIVEN,
        session: str | NotGiven = NOT_GIVEN,
        system_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/data",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "input": input,
                    "output": output,
                    "full_prompt_sent": full_prompt_sent,
                    "latency": latency,
                    "metadata": metadata,
                    "model": model,
                    "model_provider": model_provider,
                    "num_input_tokens": num_input_tokens,
                    "num_output_tokens": num_output_tokens,
                    "raw_llm_request": raw_llm_request,
                    "raw_llm_response": raw_llm_response,
                    "session": session,
                    "system_message": system_message,
                },
                data_create_params.DataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataCreateResponse,
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
    ) -> DataRetrieveResponse:
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
            f"/data/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataRetrieveResponse,
        )

    async def update(
        self,
        guid: str,
        *,
        action: str | NotGiven = NOT_GIVEN,
        app: str | NotGiven = NOT_GIVEN,
        full_prompt_sent: str | NotGiven = NOT_GIVEN,
        input: str | NotGiven = NOT_GIVEN,
        latency: float | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        model_provider: str | NotGiven = NOT_GIVEN,
        num_input_tokens: float | NotGiven = NOT_GIVEN,
        num_output_tokens: float | NotGiven = NOT_GIVEN,
        output: str | NotGiven = NOT_GIVEN,
        prompt_template: str | NotGiven = NOT_GIVEN,
        raw_llm_request: Dict[str, object] | NotGiven = NOT_GIVEN,
        raw_llm_response: str | NotGiven = NOT_GIVEN,
        session: str | NotGiven = NOT_GIVEN,
        system_message: str | NotGiven = NOT_GIVEN,
        version_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataUpdateResponse:
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
            f"/data/{guid}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "app": app,
                    "full_prompt_sent": full_prompt_sent,
                    "input": input,
                    "latency": latency,
                    "metadata": metadata,
                    "model": model,
                    "model_provider": model_provider,
                    "num_input_tokens": num_input_tokens,
                    "num_output_tokens": num_output_tokens,
                    "output": output,
                    "prompt_template": prompt_template,
                    "raw_llm_request": raw_llm_request,
                    "raw_llm_response": raw_llm_response,
                    "session": session,
                    "system_message": system_message,
                    "version_id": version_id,
                },
                data_update_params.DataUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataUpdateResponse,
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
    ) -> DataListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/data",
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
                    data_list_params.DataListParams,
                ),
            ),
            cast_to=DataListResponse,
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
    ) -> DataDeleteResponse:
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
            f"/data/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataDeleteResponse,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.create = to_raw_response_wrapper(
            data.create,
        )
        self.retrieve = to_raw_response_wrapper(
            data.retrieve,
        )
        self.update = to_raw_response_wrapper(
            data.update,
        )
        self.list = to_raw_response_wrapper(
            data.list,
        )
        self.delete = to_raw_response_wrapper(
            data.delete,
        )


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.create = async_to_raw_response_wrapper(
            data.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            data.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            data.update,
        )
        self.list = async_to_raw_response_wrapper(
            data.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data.delete,
        )


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.create = to_streamed_response_wrapper(
            data.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            data.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            data.update,
        )
        self.list = to_streamed_response_wrapper(
            data.list,
        )
        self.delete = to_streamed_response_wrapper(
            data.delete,
        )


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.create = async_to_streamed_response_wrapper(
            data.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            data.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            data.update,
        )
        self.list = async_to_streamed_response_wrapper(
            data.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data.delete,
        )
