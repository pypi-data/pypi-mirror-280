# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .types import TypesResource, AsyncTypesResource

from ..._compat import cached_property

from ...types.skill_create_response import SkillCreateResponse

from ..._utils import maybe_transform, async_maybe_transform

from typing import Iterable

from ...types.skill_retrieve_response import SkillRetrieveResponse

from ...types.skill_update_response import SkillUpdateResponse

from ...types.skill_list_response import SkillListResponse

from ...types.skill_delete_response import SkillDeleteResponse

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ...types import skill_create_params

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
from ...types import skill_create_params
from ...types import skill_update_params
from ...types import skill_list_params
from .types import (
    TypesResource,
    AsyncTypesResource,
    TypesResourceWithRawResponse,
    AsyncTypesResourceWithRawResponse,
    TypesResourceWithStreamingResponse,
    AsyncTypesResourceWithStreamingResponse,
)

__all__ = ["SkillsResource", "AsyncSkillsResource"]


class SkillsResource(SyncAPIResource):
    @cached_property
    def types(self) -> TypesResource:
        return TypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SkillsResourceWithRawResponse:
        return SkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SkillsResourceWithStreamingResponse:
        return SkillsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: str,
        metadata: Iterable[skill_create_params.Metadata] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/skills",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "metadata": metadata,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
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
    ) -> SkillRetrieveResponse:
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
            f"/skills/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillRetrieveResponse,
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
    ) -> SkillUpdateResponse:
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
            f"/skills/{guid}",
            body=maybe_transform({"name": name}, skill_update_params.SkillUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
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
    ) -> SkillListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/skills",
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
                    skill_list_params.SkillListParams,
                ),
            ),
            cast_to=SkillListResponse,
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
    ) -> SkillDeleteResponse:
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
            f"/skills/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillDeleteResponse,
        )


class AsyncSkillsResource(AsyncAPIResource):
    @cached_property
    def types(self) -> AsyncTypesResource:
        return AsyncTypesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSkillsResourceWithRawResponse:
        return AsyncSkillsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSkillsResourceWithStreamingResponse:
        return AsyncSkillsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: str,
        metadata: Iterable[skill_create_params.Metadata] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SkillCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/skills",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "metadata": metadata,
                },
                skill_create_params.SkillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillCreateResponse,
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
    ) -> SkillRetrieveResponse:
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
            f"/skills/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillRetrieveResponse,
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
    ) -> SkillUpdateResponse:
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
            f"/skills/{guid}",
            body=await async_maybe_transform({"name": name}, skill_update_params.SkillUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillUpdateResponse,
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
    ) -> SkillListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/skills",
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
                    skill_list_params.SkillListParams,
                ),
            ),
            cast_to=SkillListResponse,
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
    ) -> SkillDeleteResponse:
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
            f"/skills/{guid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SkillDeleteResponse,
        )


class SkillsResourceWithRawResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = to_raw_response_wrapper(
            skills.update,
        )
        self.list = to_raw_response_wrapper(
            skills.list,
        )
        self.delete = to_raw_response_wrapper(
            skills.delete,
        )

    @cached_property
    def types(self) -> TypesResourceWithRawResponse:
        return TypesResourceWithRawResponse(self._skills.types)


class AsyncSkillsResourceWithRawResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_raw_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            skills.update,
        )
        self.list = async_to_raw_response_wrapper(
            skills.list,
        )
        self.delete = async_to_raw_response_wrapper(
            skills.delete,
        )

    @cached_property
    def types(self) -> AsyncTypesResourceWithRawResponse:
        return AsyncTypesResourceWithRawResponse(self._skills.types)


class SkillsResourceWithStreamingResponse:
    def __init__(self, skills: SkillsResource) -> None:
        self._skills = skills

        self.create = to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            skills.update,
        )
        self.list = to_streamed_response_wrapper(
            skills.list,
        )
        self.delete = to_streamed_response_wrapper(
            skills.delete,
        )

    @cached_property
    def types(self) -> TypesResourceWithStreamingResponse:
        return TypesResourceWithStreamingResponse(self._skills.types)


class AsyncSkillsResourceWithStreamingResponse:
    def __init__(self, skills: AsyncSkillsResource) -> None:
        self._skills = skills

        self.create = async_to_streamed_response_wrapper(
            skills.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            skills.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            skills.update,
        )
        self.list = async_to_streamed_response_wrapper(
            skills.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            skills.delete,
        )

    @cached_property
    def types(self) -> AsyncTypesResourceWithStreamingResponse:
        return AsyncTypesResourceWithStreamingResponse(self._skills.types)
