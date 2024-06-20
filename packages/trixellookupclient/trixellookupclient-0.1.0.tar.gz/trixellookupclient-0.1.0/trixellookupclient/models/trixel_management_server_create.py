from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TrixelManagementServerCreate")


@_attrs_define
class TrixelManagementServerCreate:
    """ TMS initialization schema, which contains the authentication token.

        Attributes:
            id (int):
            active (bool):
            host (str):
            token (str):
     """

    id: int
    active: bool
    host: str
    token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        active = self.active

        host = self.host

        token = self.token


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "active": active,
            "host": host,
            "token": token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        active = d.pop("active")

        host = d.pop("host")

        token = d.pop("token")

        trixel_management_server_create = cls(
            id=id,
            active=active,
            host=host,
            token=token,
        )


        trixel_management_server_create.additional_properties = d
        return trixel_management_server_create

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
