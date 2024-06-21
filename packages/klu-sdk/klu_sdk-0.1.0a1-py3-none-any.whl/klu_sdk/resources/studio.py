# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.studio_chat_response import StudioChatResponse

from .._utils import maybe_transform, async_maybe_transform

from typing import Optional, Iterable, Dict, List, Union

from ..types.studio_prompt_response import StudioPromptResponse

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ..types import studio_chat_params, studio_prompt_params

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
from ..types import studio_chat_params
from ..types import studio_prompt_params

__all__ = ["StudioResource", "AsyncStudioResource"]


class StudioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StudioResourceWithRawResponse:
        return StudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StudioResourceWithStreamingResponse:
        return StudioResourceWithStreamingResponse(self)

    def chat(
        self,
        *,
        messages: Optional[Iterable[studio_chat_params.Message]],
        model_config: studio_chat_params.ModelConfig,
        model_guid: str,
        template_messages: Iterable[studio_chat_params.TemplateMessage],
        user: Optional[str],
        values: Optional[Dict[str, object]],
        action_guid: Optional[str] | NotGiven = NOT_GIVEN,
        index_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        output_format: Optional[str] | NotGiven = NOT_GIVEN,
        output_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        persist: bool | NotGiven = NOT_GIVEN,
        session: Optional[str] | NotGiven = NOT_GIVEN,
        streaming: bool | NotGiven = NOT_GIVEN,
        tool_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        version: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StudioChatResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/studio/chat",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model_config": model_config,
                    "model_guid": model_guid,
                    "template_messages": template_messages,
                    "user": user,
                    "values": values,
                    "action_guid": action_guid,
                    "index_guids": index_guids,
                    "output_format": output_format,
                    "output_instructions": output_instructions,
                    "persist": persist,
                    "session": session,
                    "streaming": streaming,
                    "tool_guids": tool_guids,
                    "version": version,
                },
                studio_chat_params.StudioChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudioChatResponse,
        )

    def prompt(
        self,
        *,
        model_config: studio_prompt_params.ModelConfig,
        model_guid: str,
        prompt: str,
        system_message: Optional[str],
        user: Optional[str],
        values: Union[Dict[str, object], str, None],
        action_guid: Optional[str] | NotGiven = NOT_GIVEN,
        files: Optional[List[str]] | NotGiven = NOT_GIVEN,
        index_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        output_format: Optional[str] | NotGiven = NOT_GIVEN,
        output_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        persist: bool | NotGiven = NOT_GIVEN,
        streaming: bool | NotGiven = NOT_GIVEN,
        tool_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        version: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StudioPromptResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/studio/prompt",
            body=maybe_transform(
                {
                    "model_config": model_config,
                    "model_guid": model_guid,
                    "prompt": prompt,
                    "system_message": system_message,
                    "user": user,
                    "values": values,
                    "action_guid": action_guid,
                    "files": files,
                    "index_guids": index_guids,
                    "output_format": output_format,
                    "output_instructions": output_instructions,
                    "persist": persist,
                    "streaming": streaming,
                    "tool_guids": tool_guids,
                    "version": version,
                },
                studio_prompt_params.StudioPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudioPromptResponse,
        )


class AsyncStudioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStudioResourceWithRawResponse:
        return AsyncStudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStudioResourceWithStreamingResponse:
        return AsyncStudioResourceWithStreamingResponse(self)

    async def chat(
        self,
        *,
        messages: Optional[Iterable[studio_chat_params.Message]],
        model_config: studio_chat_params.ModelConfig,
        model_guid: str,
        template_messages: Iterable[studio_chat_params.TemplateMessage],
        user: Optional[str],
        values: Optional[Dict[str, object]],
        action_guid: Optional[str] | NotGiven = NOT_GIVEN,
        index_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        output_format: Optional[str] | NotGiven = NOT_GIVEN,
        output_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        persist: bool | NotGiven = NOT_GIVEN,
        session: Optional[str] | NotGiven = NOT_GIVEN,
        streaming: bool | NotGiven = NOT_GIVEN,
        tool_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        version: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StudioChatResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/studio/chat",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model_config": model_config,
                    "model_guid": model_guid,
                    "template_messages": template_messages,
                    "user": user,
                    "values": values,
                    "action_guid": action_guid,
                    "index_guids": index_guids,
                    "output_format": output_format,
                    "output_instructions": output_instructions,
                    "persist": persist,
                    "session": session,
                    "streaming": streaming,
                    "tool_guids": tool_guids,
                    "version": version,
                },
                studio_chat_params.StudioChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudioChatResponse,
        )

    async def prompt(
        self,
        *,
        model_config: studio_prompt_params.ModelConfig,
        model_guid: str,
        prompt: str,
        system_message: Optional[str],
        user: Optional[str],
        values: Union[Dict[str, object], str, None],
        action_guid: Optional[str] | NotGiven = NOT_GIVEN,
        files: Optional[List[str]] | NotGiven = NOT_GIVEN,
        index_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        output_format: Optional[str] | NotGiven = NOT_GIVEN,
        output_instructions: Optional[str] | NotGiven = NOT_GIVEN,
        persist: bool | NotGiven = NOT_GIVEN,
        streaming: bool | NotGiven = NOT_GIVEN,
        tool_guids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        version: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StudioPromptResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/studio/prompt",
            body=await async_maybe_transform(
                {
                    "model_config": model_config,
                    "model_guid": model_guid,
                    "prompt": prompt,
                    "system_message": system_message,
                    "user": user,
                    "values": values,
                    "action_guid": action_guid,
                    "files": files,
                    "index_guids": index_guids,
                    "output_format": output_format,
                    "output_instructions": output_instructions,
                    "persist": persist,
                    "streaming": streaming,
                    "tool_guids": tool_guids,
                    "version": version,
                },
                studio_prompt_params.StudioPromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StudioPromptResponse,
        )


class StudioResourceWithRawResponse:
    def __init__(self, studio: StudioResource) -> None:
        self._studio = studio

        self.chat = to_raw_response_wrapper(
            studio.chat,
        )
        self.prompt = to_raw_response_wrapper(
            studio.prompt,
        )


class AsyncStudioResourceWithRawResponse:
    def __init__(self, studio: AsyncStudioResource) -> None:
        self._studio = studio

        self.chat = async_to_raw_response_wrapper(
            studio.chat,
        )
        self.prompt = async_to_raw_response_wrapper(
            studio.prompt,
        )


class StudioResourceWithStreamingResponse:
    def __init__(self, studio: StudioResource) -> None:
        self._studio = studio

        self.chat = to_streamed_response_wrapper(
            studio.chat,
        )
        self.prompt = to_streamed_response_wrapper(
            studio.prompt,
        )


class AsyncStudioResourceWithStreamingResponse:
    def __init__(self, studio: AsyncStudioResource) -> None:
        self._studio = studio

        self.chat = async_to_streamed_response_wrapper(
            studio.chat,
        )
        self.prompt = async_to_streamed_response_wrapper(
            studio.prompt,
        )
