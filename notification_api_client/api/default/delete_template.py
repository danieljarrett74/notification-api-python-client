from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client, AwsSignedClient
from ...models.delete_template_response import DeleteTemplateResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    template_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/template/{templateId}".format(client.base_url, templateId=template_id)

    if not isinstance(client, AwsSignedClient):
        headers: Dict[str, str] = client.get_headers()
    else: 
        headers: Dict[str, str] = client.get_signed_headers(
            method="DELETE",
            url=url
        )
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[DeleteTemplateResponse, Error]]:
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = DeleteTemplateResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DeleteTemplateResponse, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    template_id: str,
    *,
    client: Client,
) -> Response[Union[DeleteTemplateResponse, Error]]:
    """
    Args:
        template_id (str):

    Returns:
        Response[Union[DeleteTemplateResponse, Error]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    template_id: str,
    *,
    client: Client,
) -> Optional[Union[DeleteTemplateResponse, Error]]:
    """
    Args:
        template_id (str):

    Returns:
        Response[Union[DeleteTemplateResponse, Error]]
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: Client,
) -> Response[Union[DeleteTemplateResponse, Error]]:
    """
    Args:
        template_id (str):

    Returns:
        Response[Union[DeleteTemplateResponse, Error]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    template_id: str,
    *,
    client: Client,
) -> Optional[Union[DeleteTemplateResponse, Error]]:
    """
    Args:
        template_id (str):

    Returns:
        Response[Union[DeleteTemplateResponse, Error]]
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
        )
    ).parsed
