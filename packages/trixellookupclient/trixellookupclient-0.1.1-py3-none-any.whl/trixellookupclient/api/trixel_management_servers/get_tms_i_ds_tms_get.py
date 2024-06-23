from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Union
from typing import cast, Union
from typing import Dict
from typing import cast, List
from ...types import UNSET, Unset
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    *,
    active: Union[None, Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    json_active: Union[None, Unset, bool]
    if isinstance(active, Unset):
        json_active = UNSET
    else:
        json_active = active
    params["active"] = json_active

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/TMS",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List[int]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[int], response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List[int]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[None, Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Response[Union[HTTPValidationError, List[int]]]:
    """ Get a list of all registered trixel management server IDs.

     Get a list of all registered trixel management server IDs.

    Args:
        active (Union[None, Unset, bool]): Filters results by the TMS state.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[int]]]
     """


    kwargs = _get_kwargs(
        active=active,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[None, Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Optional[Union[HTTPValidationError, List[int]]]:
    """ Get a list of all registered trixel management server IDs.

     Get a list of all registered trixel management server IDs.

    Args:
        active (Union[None, Unset, bool]): Filters results by the TMS state.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[int]]
     """


    return sync_detailed(
        client=client,
active=active,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[None, Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Response[Union[HTTPValidationError, List[int]]]:
    """ Get a list of all registered trixel management server IDs.

     Get a list of all registered trixel management server IDs.

    Args:
        active (Union[None, Unset, bool]): Filters results by the TMS state.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[int]]]
     """


    kwargs = _get_kwargs(
        active=active,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[None, Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Optional[Union[HTTPValidationError, List[int]]]:
    """ Get a list of all registered trixel management server IDs.

     Get a list of all registered trixel management server IDs.

    Args:
        active (Union[None, Unset, bool]): Filters results by the TMS state.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[int]]
     """


    return (await asyncio_detailed(
        client=client,
active=active,
limit=limit,
offset=offset,

    )).parsed
