from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.trixel_management_server_create import TrixelManagementServerCreate
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    *,
    host: str,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    params["host"] = host


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/TMS",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrixelManagementServerCreate.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,

) -> Response[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]:
    """ Add a TMS to this TLS.

     Add a trixel management server to this trixel lookup server.

    Returns TMS details including the authentication token. Store this token properly, it is only sent
    once.
    Requires a valid response from the TMS when requesting the /ping endpoint.

    Args:
        host (str): Address under which the TMS is available.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]
     """


    kwargs = _get_kwargs(
        host=host,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,

) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]:
    """ Add a TMS to this TLS.

     Add a trixel management server to this trixel lookup server.

    Returns TMS details including the authentication token. Store this token properly, it is only sent
    once.
    Requires a valid response from the TMS when requesting the /ping endpoint.

    Args:
        host (str): Address under which the TMS is available.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelManagementServerCreate]
     """


    return sync_detailed(
        client=client,
host=host,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,

) -> Response[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]:
    """ Add a TMS to this TLS.

     Add a trixel management server to this trixel lookup server.

    Returns TMS details including the authentication token. Store this token properly, it is only sent
    once.
    Requires a valid response from the TMS when requesting the /ping endpoint.

    Args:
        host (str): Address under which the TMS is available.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]
     """


    kwargs = _get_kwargs(
        host=host,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,

) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServerCreate]]:
    """ Add a TMS to this TLS.

     Add a trixel management server to this trixel lookup server.

    Returns TMS details including the authentication token. Store this token properly, it is only sent
    once.
    Requires a valid response from the TMS when requesting the /ping endpoint.

    Args:
        host (str): Address under which the TMS is available.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelManagementServerCreate]
     """


    return (await asyncio_detailed(
        client=client,
host=host,

    )).parsed
