from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client,AwsSignedClient
from ...models.delete_sender_response import DeleteSenderResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    sender_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sender/{senderId}".format(client.base_url, senderId=sender_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[DeleteSenderResponse, Error]]:
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = DeleteSenderResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[DeleteSenderResponse, Error]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    sender_id: str,
    *,
    client: Client,
) -> Response[Union[DeleteSenderResponse, Error]]:
    """
    Args:
        sender_id (str):

    Returns:
        Response[Union[DeleteSenderResponse, Error]]
    """

    kwargs = _get_kwargs(
        sender_id=sender_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    sender_id: str,
    *,
    client: Client,
) -> Optional[Union[DeleteSenderResponse, Error]]:
    """
    Args:
        sender_id (str):

    Returns:
        Response[Union[DeleteSenderResponse, Error]]
    """

    return sync_detailed(
        sender_id=sender_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sender_id: str,
    *,
    client: Client,
) -> Response[Union[DeleteSenderResponse, Error]]:
    """
    Args:
        sender_id (str):

    Returns:
        Response[Union[DeleteSenderResponse, Error]]
    """

    kwargs = _get_kwargs(
        sender_id=sender_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    sender_id: str,
    *,
    client: Client,
) -> Optional[Union[DeleteSenderResponse, Error]]:
    """
    Args:
        sender_id (str):

    Returns:
        Response[Union[DeleteSenderResponse, Error]]
    """

    return (
        await asyncio_detailed(
            sender_id=sender_id,
            client=client,
        )
    ).parsed
