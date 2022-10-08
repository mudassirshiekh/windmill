from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_completed_job_response_200 import GetCompletedJobResponse200
from ...types import Response


def _get_kwargs(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/w/{workspace}/jobs/completed/get/{id}".format(client.base_url, workspace=workspace, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetCompletedJobResponse200]:
    if response.status_code == 200:
        response_200 = GetCompletedJobResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetCompletedJobResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Response[GetCompletedJobResponse200]:
    """get completed job

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[GetCompletedJobResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Optional[GetCompletedJobResponse200]:
    """get completed job

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[GetCompletedJobResponse200]
    """

    return sync_detailed(
        workspace=workspace,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Response[GetCompletedJobResponse200]:
    """get completed job

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[GetCompletedJobResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace: str,
    id: str,
    *,
    client: Client,
) -> Optional[GetCompletedJobResponse200]:
    """get completed job

    Args:
        workspace (str):
        id (str):

    Returns:
        Response[GetCompletedJobResponse200]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            id=id,
            client=client,
        )
    ).parsed
