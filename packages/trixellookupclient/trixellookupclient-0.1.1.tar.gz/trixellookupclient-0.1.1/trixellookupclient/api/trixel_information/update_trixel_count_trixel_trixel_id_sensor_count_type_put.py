from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.measurement_type import MeasurementType
from typing import cast
from typing import Dict
from ...models.trixel_map_update import TrixelMapUpdate
from ...models.http_validation_error import HTTPValidationError



def _get_kwargs(
    trixel_id: int,
    type: MeasurementType,
    *,
    sensor_count: int,
    token: str,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["token"] = token



    

    params: Dict[str, Any] = {}

    params["sensor_count"] = sensor_count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/trixel/{trixel_id}/sensor_count/{type}".format(trixel_id=trixel_id,type=type,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, TrixelMapUpdate]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrixelMapUpdate.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, TrixelMapUpdate]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trixel_id: int,
    type: MeasurementType,
    *,
    client: Union[AuthenticatedClient, Client],
    sensor_count: int,
    token: str,

) -> Response[Union[Any, HTTPValidationError, TrixelMapUpdate]]:
    """ Update the sensor count for a given trixel and type.

     Update (or insert new) trixel sensor count within the DB.

    Args:
        trixel_id (int): The Trixel id for which the sensor count is updated.
        type (MeasurementType): Supported measurement types.
        sensor_count (int): The new number of sensors for the given type within the trixel.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelMapUpdate]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,
type=type,
sensor_count=sensor_count,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trixel_id: int,
    type: MeasurementType,
    *,
    client: Union[AuthenticatedClient, Client],
    sensor_count: int,
    token: str,

) -> Optional[Union[Any, HTTPValidationError, TrixelMapUpdate]]:
    """ Update the sensor count for a given trixel and type.

     Update (or insert new) trixel sensor count within the DB.

    Args:
        trixel_id (int): The Trixel id for which the sensor count is updated.
        type (MeasurementType): Supported measurement types.
        sensor_count (int): The new number of sensors for the given type within the trixel.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelMapUpdate]
     """


    return sync_detailed(
        trixel_id=trixel_id,
type=type,
client=client,
sensor_count=sensor_count,
token=token,

    ).parsed

async def asyncio_detailed(
    trixel_id: int,
    type: MeasurementType,
    *,
    client: Union[AuthenticatedClient, Client],
    sensor_count: int,
    token: str,

) -> Response[Union[Any, HTTPValidationError, TrixelMapUpdate]]:
    """ Update the sensor count for a given trixel and type.

     Update (or insert new) trixel sensor count within the DB.

    Args:
        trixel_id (int): The Trixel id for which the sensor count is updated.
        type (MeasurementType): Supported measurement types.
        sensor_count (int): The new number of sensors for the given type within the trixel.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, TrixelMapUpdate]]
     """


    kwargs = _get_kwargs(
        trixel_id=trixel_id,
type=type,
sensor_count=sensor_count,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trixel_id: int,
    type: MeasurementType,
    *,
    client: Union[AuthenticatedClient, Client],
    sensor_count: int,
    token: str,

) -> Optional[Union[Any, HTTPValidationError, TrixelMapUpdate]]:
    """ Update the sensor count for a given trixel and type.

     Update (or insert new) trixel sensor count within the DB.

    Args:
        trixel_id (int): The Trixel id for which the sensor count is updated.
        type (MeasurementType): Supported measurement types.
        sensor_count (int): The new number of sensors for the given type within the trixel.
        token (str): TMS authentication token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, TrixelMapUpdate]
     """


    return (await asyncio_detailed(
        trixel_id=trixel_id,
type=type,
client=client,
sensor_count=sensor_count,
token=token,

    )).parsed
