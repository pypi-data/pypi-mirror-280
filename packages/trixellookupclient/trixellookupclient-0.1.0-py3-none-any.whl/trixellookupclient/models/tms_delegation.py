from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Union
from ..types import UNSET, Unset






T = TypeVar("T", bound="TMSDelegation")


@_attrs_define
class TMSDelegation:
    """ Schema which describes a TMS trixel delegation.

        Attributes:
            tms_id (int):
            trixel_id (int):
            exclude (Union[Unset, bool]):  Default: False.
     """

    tms_id: int
    trixel_id: int
    exclude: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        tms_id = self.tms_id

        trixel_id = self.trixel_id

        exclude = self.exclude


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tms_id": tms_id,
            "trixel_id": trixel_id,
        })
        if exclude is not UNSET:
            field_dict["exclude"] = exclude

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tms_id = d.pop("tms_id")

        trixel_id = d.pop("trixel_id")

        exclude = d.pop("exclude", UNSET)

        tms_delegation = cls(
            tms_id=tms_id,
            trixel_id=trixel_id,
            exclude=exclude,
        )


        tms_delegation.additional_properties = d
        return tms_delegation

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
