from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error import Error
from ...models.put_template_response import PutTemplateResponse
from ...models.template import Template
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Template,
) -> Dict[str, Any]:
    url = "{}/template".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Error, PutTemplateResponse]]:
    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = PutTemplateResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Error, PutTemplateResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Template,
) -> Response[Union[Error, PutTemplateResponse]]:
    """
    Args:
        json_body (Template):

    Returns:
        Response[Union[Error, PutTemplateResponse]]
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
    json_body: Template,
) -> Optional[Union[Error, PutTemplateResponse]]:
    """
    Args:
        json_body (Template):

    Returns:
        Response[Union[Error, PutTemplateResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Template,
) -> Response[Union[Error, PutTemplateResponse]]:
    """
    Args:
        json_body (Template):

    Returns:
        Response[Union[Error, PutTemplateResponse]]
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
    json_body: Template,
) -> Optional[Union[Error, PutTemplateResponse]]:
    """
    Args:
        json_body (Template):

    Returns:
        Response[Union[Error, PutTemplateResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
