from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.measurement_type import MeasurementType
from typing import Dict
from typing import Union
from typing import cast, List
from ...types import UNSET, Unset
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    trixel_id: int,
    *,
    types: Union[Unset, List[MeasurementType]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    json_types: Union[Unset, List[str]] = UNSET
    if not isinstance(types, Unset):
        json_types = []
        for types_item_data in types:
            types_item = types_item_data.value
            json_types.append(types_item)


    params["types"] = json_types

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trixel/{trixel_id}".format(trixel_id=trixel_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, List[int]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[int], response.json())

        return response_200
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, List[int]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementType]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Response[Union[Any, HTTPValidationError, List[int]]]:
    """ Retrieve an overview of sub-trixels which contain at least one sensors of the specified types.

     Get a list of sub-trixel ids with at least one sensor (filtered by measurement type).

    Args:
        trixel_id (int): Root trixel which makes up the search space for sub-trixels.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List[int]]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,
types=types,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementType]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Optional[Union[Any, HTTPValidationError, List[int]]]:
    """ Retrieve an overview of sub-trixels which contain at least one sensors of the specified types.

     Get a list of sub-trixel ids with at least one sensor (filtered by measurement type).

    Args:
        trixel_id (int): Root trixel which makes up the search space for sub-trixels.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, List[int]]
     """


    return sync_detailed(
        trixel_id=trixel_id,
client=client,
types=types,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementType]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Response[Union[Any, HTTPValidationError, List[int]]]:
    """ Retrieve an overview of sub-trixels which contain at least one sensors of the specified types.

     Get a list of sub-trixel ids with at least one sensor (filtered by measurement type).

    Args:
        trixel_id (int): Root trixel which makes up the search space for sub-trixels.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List[int]]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,
types=types,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementType]] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,

) -> Optional[Union[Any, HTTPValidationError, List[int]]]:
    """ Retrieve an overview of sub-trixels which contain at least one sensors of the specified types.

     Get a list of sub-trixel ids with at least one sensor (filtered by measurement type).

    Args:
        trixel_id (int): Root trixel which makes up the search space for sub-trixels.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.
        limit (Union[Unset, int]): Limits the number of results. Default: 100.
        offset (Union[Unset, int]): Skip the first n results. Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, List[int]]
     """


    return (await asyncio_detailed(
        trixel_id=trixel_id,
client=client,
types=types,
limit=limit,
offset=offset,

    )).parsed
