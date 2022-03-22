from typing import Any, Dict, Optional, Union

import httpx
import json 
from ...client import Client, AwsSignedClient
from ...models.error import Error
from ...models.message import Message
from ...models.send_response import SendResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Message,
) -> Dict[str, Any]:
    url = "{}/send".format(client.base_url)

    
    if not isinstance(client, AwsSignedClient):
        headers: Dict[str, str] = client.get_headers()
    else: 
        headers: Dict[str, str] = client.get_signed_headers(
            method="POST",
            url=url, 
            payload=json.dumps(json_body.to_dict())
        )
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, SendResponse]]:
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = SendResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, SendResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Message,
) -> Response[Union[Error, SendResponse]]:
    """
    Args:
        json_body (Message):

    Returns:
        Response[Union[Error, SendResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Message,
) -> Optional[Union[Error, SendResponse]]:
    """
    Args:
        json_body (Message):

    Returns:
        Response[Union[Error, SendResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Message,
) -> Response[Union[Error, SendResponse]]:
    """
    Args:
        json_body (Message):

    Returns:
        Response[Union[Error, SendResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Message,
) -> Optional[Union[Error, SendResponse]]:
    """
    Args:
        json_body (Message):

    Returns:
        Response[Union[Error, SendResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
