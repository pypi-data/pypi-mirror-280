# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

import os

from ._streaming import AsyncStream as AsyncStream, Stream as Stream

from ._exceptions import SDKError, APIStatusError

from typing_extensions import override, Self

from typing import Any

from ._utils import get_async_library

from . import _exceptions

import os
import asyncio
import warnings
from typing import Optional, Union, Dict, Any, Mapping, overload, cast
from typing_extensions import Literal

import httpx

from ._version import __version__
from ._qs import Querystring
from .types import shared_params
from ._utils import (
    extract_files,
    maybe_transform,
    required_args,
    deepcopy_minimal,
    maybe_coerce_integer,
    maybe_coerce_float,
    maybe_coerce_boolean,
    is_given,
)
from ._types import (
    Omit,
    NotGiven,
    Timeout,
    Transport,
    ProxiesTypes,
    RequestOptions,
    Headers,
    NoneType,
    Query,
    Body,
    NOT_GIVEN,
)
from ._base_client import (
    DEFAULT_CONNECTION_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    ResponseT,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from . import resources

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "SDK",
    "AsyncSDK",
    "Client",
    "AsyncClient",
]


class SDK(SyncAPIClient):
    apps: resources.AppsResource
    actions: resources.ActionsResource
    studio: resources.StudioResource
    contexts: resources.ContextsResource
    data: resources.DataResource
    datasets: resources.DatasetsResource
    evals: resources.EvalsResource
    experiments: resources.ExperimentsResource
    feedback: resources.FeedbackResource
    finetunes: resources.FinetunesResource
    models: resources.ModelsResource
    sessions: resources.SessionsResource
    skills: resources.SkillsResource
    workflows: resources.WorkflowsResource
    workspaces: resources.WorkspacesResource
    providers: resources.ProvidersResource
    with_raw_response: SDKWithRawResponse
    with_streaming_response: SDKWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous sdk client instance.

        This automatically infers the `bearer_token` argument from the `SDK_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("SDK_BEARER_TOKEN")
        if bearer_token is None:
            raise SDKError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the SDK_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("SDK_BASE_URL")
        if base_url is None:
            base_url = f"/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.apps = resources.AppsResource(self)
        self.actions = resources.ActionsResource(self)
        self.studio = resources.StudioResource(self)
        self.contexts = resources.ContextsResource(self)
        self.data = resources.DataResource(self)
        self.datasets = resources.DatasetsResource(self)
        self.evals = resources.EvalsResource(self)
        self.experiments = resources.ExperimentsResource(self)
        self.feedback = resources.FeedbackResource(self)
        self.finetunes = resources.FinetunesResource(self)
        self.models = resources.ModelsResource(self)
        self.sessions = resources.SessionsResource(self)
        self.skills = resources.SkillsResource(self)
        self.workflows = resources.WorkflowsResource(self)
        self.workspaces = resources.WorkspacesResource(self)
        self.providers = resources.ProvidersResource(self)
        self.with_raw_response = SDKWithRawResponse(self)
        self.with_streaming_response = SDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSDK(AsyncAPIClient):
    apps: resources.AsyncAppsResource
    actions: resources.AsyncActionsResource
    studio: resources.AsyncStudioResource
    contexts: resources.AsyncContextsResource
    data: resources.AsyncDataResource
    datasets: resources.AsyncDatasetsResource
    evals: resources.AsyncEvalsResource
    experiments: resources.AsyncExperimentsResource
    feedback: resources.AsyncFeedbackResource
    finetunes: resources.AsyncFinetunesResource
    models: resources.AsyncModelsResource
    sessions: resources.AsyncSessionsResource
    skills: resources.AsyncSkillsResource
    workflows: resources.AsyncWorkflowsResource
    workspaces: resources.AsyncWorkspacesResource
    providers: resources.AsyncProvidersResource
    with_raw_response: AsyncSDKWithRawResponse
    with_streaming_response: AsyncSDKWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async sdk client instance.

        This automatically infers the `bearer_token` argument from the `SDK_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("SDK_BEARER_TOKEN")
        if bearer_token is None:
            raise SDKError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the SDK_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("SDK_BASE_URL")
        if base_url is None:
            base_url = f"/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.apps = resources.AsyncAppsResource(self)
        self.actions = resources.AsyncActionsResource(self)
        self.studio = resources.AsyncStudioResource(self)
        self.contexts = resources.AsyncContextsResource(self)
        self.data = resources.AsyncDataResource(self)
        self.datasets = resources.AsyncDatasetsResource(self)
        self.evals = resources.AsyncEvalsResource(self)
        self.experiments = resources.AsyncExperimentsResource(self)
        self.feedback = resources.AsyncFeedbackResource(self)
        self.finetunes = resources.AsyncFinetunesResource(self)
        self.models = resources.AsyncModelsResource(self)
        self.sessions = resources.AsyncSessionsResource(self)
        self.skills = resources.AsyncSkillsResource(self)
        self.workflows = resources.AsyncWorkflowsResource(self)
        self.workspaces = resources.AsyncWorkspacesResource(self)
        self.providers = resources.AsyncProvidersResource(self)
        self.with_raw_response = AsyncSDKWithRawResponse(self)
        self.with_streaming_response = AsyncSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SDKWithRawResponse:
    def __init__(self, client: SDK) -> None:
        self.apps = resources.AppsResourceWithRawResponse(client.apps)
        self.actions = resources.ActionsResourceWithRawResponse(client.actions)
        self.studio = resources.StudioResourceWithRawResponse(client.studio)
        self.contexts = resources.ContextsResourceWithRawResponse(client.contexts)
        self.data = resources.DataResourceWithRawResponse(client.data)
        self.datasets = resources.DatasetsResourceWithRawResponse(client.datasets)
        self.evals = resources.EvalsResourceWithRawResponse(client.evals)
        self.experiments = resources.ExperimentsResourceWithRawResponse(client.experiments)
        self.feedback = resources.FeedbackResourceWithRawResponse(client.feedback)
        self.finetunes = resources.FinetunesResourceWithRawResponse(client.finetunes)
        self.models = resources.ModelsResourceWithRawResponse(client.models)
        self.sessions = resources.SessionsResourceWithRawResponse(client.sessions)
        self.skills = resources.SkillsResourceWithRawResponse(client.skills)
        self.workflows = resources.WorkflowsResourceWithRawResponse(client.workflows)
        self.workspaces = resources.WorkspacesResourceWithRawResponse(client.workspaces)
        self.providers = resources.ProvidersResourceWithRawResponse(client.providers)


class AsyncSDKWithRawResponse:
    def __init__(self, client: AsyncSDK) -> None:
        self.apps = resources.AsyncAppsResourceWithRawResponse(client.apps)
        self.actions = resources.AsyncActionsResourceWithRawResponse(client.actions)
        self.studio = resources.AsyncStudioResourceWithRawResponse(client.studio)
        self.contexts = resources.AsyncContextsResourceWithRawResponse(client.contexts)
        self.data = resources.AsyncDataResourceWithRawResponse(client.data)
        self.datasets = resources.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.evals = resources.AsyncEvalsResourceWithRawResponse(client.evals)
        self.experiments = resources.AsyncExperimentsResourceWithRawResponse(client.experiments)
        self.feedback = resources.AsyncFeedbackResourceWithRawResponse(client.feedback)
        self.finetunes = resources.AsyncFinetunesResourceWithRawResponse(client.finetunes)
        self.models = resources.AsyncModelsResourceWithRawResponse(client.models)
        self.sessions = resources.AsyncSessionsResourceWithRawResponse(client.sessions)
        self.skills = resources.AsyncSkillsResourceWithRawResponse(client.skills)
        self.workflows = resources.AsyncWorkflowsResourceWithRawResponse(client.workflows)
        self.workspaces = resources.AsyncWorkspacesResourceWithRawResponse(client.workspaces)
        self.providers = resources.AsyncProvidersResourceWithRawResponse(client.providers)


class SDKWithStreamedResponse:
    def __init__(self, client: SDK) -> None:
        self.apps = resources.AppsResourceWithStreamingResponse(client.apps)
        self.actions = resources.ActionsResourceWithStreamingResponse(client.actions)
        self.studio = resources.StudioResourceWithStreamingResponse(client.studio)
        self.contexts = resources.ContextsResourceWithStreamingResponse(client.contexts)
        self.data = resources.DataResourceWithStreamingResponse(client.data)
        self.datasets = resources.DatasetsResourceWithStreamingResponse(client.datasets)
        self.evals = resources.EvalsResourceWithStreamingResponse(client.evals)
        self.experiments = resources.ExperimentsResourceWithStreamingResponse(client.experiments)
        self.feedback = resources.FeedbackResourceWithStreamingResponse(client.feedback)
        self.finetunes = resources.FinetunesResourceWithStreamingResponse(client.finetunes)
        self.models = resources.ModelsResourceWithStreamingResponse(client.models)
        self.sessions = resources.SessionsResourceWithStreamingResponse(client.sessions)
        self.skills = resources.SkillsResourceWithStreamingResponse(client.skills)
        self.workflows = resources.WorkflowsResourceWithStreamingResponse(client.workflows)
        self.workspaces = resources.WorkspacesResourceWithStreamingResponse(client.workspaces)
        self.providers = resources.ProvidersResourceWithStreamingResponse(client.providers)


class AsyncSDKWithStreamedResponse:
    def __init__(self, client: AsyncSDK) -> None:
        self.apps = resources.AsyncAppsResourceWithStreamingResponse(client.apps)
        self.actions = resources.AsyncActionsResourceWithStreamingResponse(client.actions)
        self.studio = resources.AsyncStudioResourceWithStreamingResponse(client.studio)
        self.contexts = resources.AsyncContextsResourceWithStreamingResponse(client.contexts)
        self.data = resources.AsyncDataResourceWithStreamingResponse(client.data)
        self.datasets = resources.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.evals = resources.AsyncEvalsResourceWithStreamingResponse(client.evals)
        self.experiments = resources.AsyncExperimentsResourceWithStreamingResponse(client.experiments)
        self.feedback = resources.AsyncFeedbackResourceWithStreamingResponse(client.feedback)
        self.finetunes = resources.AsyncFinetunesResourceWithStreamingResponse(client.finetunes)
        self.models = resources.AsyncModelsResourceWithStreamingResponse(client.models)
        self.sessions = resources.AsyncSessionsResourceWithStreamingResponse(client.sessions)
        self.skills = resources.AsyncSkillsResourceWithStreamingResponse(client.skills)
        self.workflows = resources.AsyncWorkflowsResourceWithStreamingResponse(client.workflows)
        self.workspaces = resources.AsyncWorkspacesResourceWithStreamingResponse(client.workspaces)
        self.providers = resources.AsyncProvidersResourceWithStreamingResponse(client.providers)


Client = SDK

AsyncClient = AsyncSDK
