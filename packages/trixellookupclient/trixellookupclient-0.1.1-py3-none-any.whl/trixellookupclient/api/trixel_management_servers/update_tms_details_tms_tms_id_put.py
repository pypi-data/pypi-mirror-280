from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from typing import cast
from typing import Dict
from ...models.trixel_management_server import TrixelManagementServer



def _get_kwargs(
    tms_id: int,
    *,
    host: str,
    token: str,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["token"] = token



    

    params: Dict[str, Any] = {}

    params["host"] = host


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/TMS/{tms_id}".format(tms_id=tms_id,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrixelManagementServer.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,
    token: str,

) -> Response[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Update TMS details.

     Update the details of the provided TMS.

    Args:
        tms_id (int): TMS to which changes apply.
        host (str): New address under which the TMS is available.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelManagementServer]]
     """


    kwargs = _get_kwargs(
        tms_id=tms_id,
host=host,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,
    token: str,

) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Update TMS details.

     Update the details of the provided TMS.

    Args:
        tms_id (int): TMS to which changes apply.
        host (str): New address under which the TMS is available.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelManagementServer]
     """


    return sync_detailed(
        tms_id=tms_id,
client=client,
host=host,
token=token,

    ).parsed

async def asyncio_detailed(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,
    token: str,

) -> Response[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Update TMS details.

     Update the details of the provided TMS.

    Args:
        tms_id (int): TMS to which changes apply.
        host (str): New address under which the TMS is available.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelManagementServer]]
     """


    kwargs = _get_kwargs(
        tms_id=tms_id,
host=host,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    host: str,
    token: str,

) -> Optional[Union[Any, HTTPValidationError, TrixelManagementServer]]:
    """ Update TMS details.

     Update the details of the provided TMS.

    Args:
        tms_id (int): TMS to which changes apply.
        host (str): New address under which the TMS is available.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelManagementServer]
     """


    return (await asyncio_detailed(
        tms_id=tms_id,
client=client,
host=host,
token=token,

    )).parsed
