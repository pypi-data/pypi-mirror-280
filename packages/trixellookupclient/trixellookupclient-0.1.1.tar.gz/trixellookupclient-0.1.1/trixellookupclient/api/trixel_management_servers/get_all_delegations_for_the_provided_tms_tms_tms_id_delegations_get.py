from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.http_validation_error import HTTPValidationError
from typing import cast, List
from ...models.tms_delegation import TMSDelegation



def _get_kwargs(
    tms_id: int,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/TMS/{tms_id}/delegations".format(tms_id=tms_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError, List['TMSDelegation']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = TMSDelegation.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError, List['TMSDelegation']]]:
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

) -> Response[Union[Any, HTTPValidationError, List['TMSDelegation']]]:
    """ Get all delegations for the provided TMS, including other TMSs which manage excluded trixels.

     Get the delegations and exceptions associated with this TMS.

    Args:
        tms_id (int): ID of the desired TMS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['TMSDelegation']]]
     """


    kwargs = _get_kwargs(
        tms_id=tms_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, HTTPValidationError, List['TMSDelegation']]]:
    """ Get all delegations for the provided TMS, including other TMSs which manage excluded trixels.

     Get the delegations and exceptions associated with this TMS.

    Args:
        tms_id (int): ID of the desired TMS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, List['TMSDelegation']]
     """


    return sync_detailed(
        tms_id=tms_id,
client=client,

    ).parsed

async def asyncio_detailed(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, HTTPValidationError, List['TMSDelegation']]]:
    """ Get all delegations for the provided TMS, including other TMSs which manage excluded trixels.

     Get the delegations and exceptions associated with this TMS.

    Args:
        tms_id (int): ID of the desired TMS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['TMSDelegation']]]
     """


    kwargs = _get_kwargs(
        tms_id=tms_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tms_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, HTTPValidationError, List['TMSDelegation']]]:
    """ Get all delegations for the provided TMS, including other TMSs which manage excluded trixels.

     Get the delegations and exceptions associated with this TMS.

    Args:
        tms_id (int): ID of the desired TMS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, List['TMSDelegation']]
     """


    return (await asyncio_detailed(
        tms_id=tms_id,
client=client,

    )).parsed
