from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.measurement_type import MeasurementType
from ...models.trixel_map import TrixelMap
from typing import Dict
from typing import Union
from typing import cast, List
from ...types import UNSET, Unset
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    trixel_id: int,
    *,
    types: Union[Unset, List[MeasurementType]] = UNSET,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    json_types: Union[Unset, List[str]] = UNSET
    if not isinstance(types, Unset):
        json_types = []
        for types_item_data in types:
            types_item = types_item_data.value
            json_types.append(types_item)


    params["types"] = json_types


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/trixel/{trixel_id}/sensor_count".format(trixel_id=trixel_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, TrixelMap]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrixelMap.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, TrixelMap]]:
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

) -> Response[Union[Any, HTTPValidationError, TrixelMap]]:
    """ Get the sensor count within a trixel per measurement type.

     Get the sensor count for a trixel for different measurement types.

    Args:
        trixel_id (int): The id of the trixel for which the sensor count is to be determined.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelMap]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,
types=types,

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

) -> Optional[Union[Any, HTTPValidationError, TrixelMap]]:
    """ Get the sensor count within a trixel per measurement type.

     Get the sensor count for a trixel for different measurement types.

    Args:
        trixel_id (int): The id of the trixel for which the sensor count is to be determined.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelMap]
     """


    return sync_detailed(
        trixel_id=trixel_id,
client=client,
types=types,

    ).parsed

async def asyncio_detailed(
    trixel_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    types: Union[Unset, List[MeasurementType]] = UNSET,

) -> Response[Union[Any, HTTPValidationError, TrixelMap]]:
    """ Get the sensor count within a trixel per measurement type.

     Get the sensor count for a trixel for different measurement types.

    Args:
        trixel_id (int): The id of the trixel for which the sensor count is to be determined.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelMap]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,
types=types,

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

) -> Optional[Union[Any, HTTPValidationError, TrixelMap]]:
    """ Get the sensor count within a trixel per measurement type.

     Get the sensor count for a trixel for different measurement types.

    Args:
        trixel_id (int): The id of the trixel for which the sensor count is to be determined.
        types (Union[Unset, List[MeasurementType]]): List of measurement types which restrict
            results. If none are provided, all types are used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelMap]
     """


    return (await asyncio_detailed(
        trixel_id=trixel_id,
client=client,
types=types,

    )).parsed
