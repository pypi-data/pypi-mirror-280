from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Dict

if TYPE_CHECKING:
  from ..models.trixel_map_sensor_counts import TrixelMapSensorCounts





T = TypeVar("T", bound="TrixelMap")


@_attrs_define
class TrixelMap:
    """ Schema for reading from the trixel map.

        Attributes:
            id (int):
            sensor_counts (TrixelMapSensorCounts):
     """

    id: int
    sensor_counts: 'TrixelMapSensorCounts'
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.trixel_map_sensor_counts import TrixelMapSensorCounts
        id = self.id

        sensor_counts = self.sensor_counts.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "sensor_counts": sensor_counts,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trixel_map_sensor_counts import TrixelMapSensorCounts
        d = src_dict.copy()
        id = d.pop("id")

        sensor_counts = TrixelMapSensorCounts.from_dict(d.pop("sensor_counts"))




        trixel_map = cls(
            id=id,
            sensor_counts=sensor_counts,
        )


        trixel_map.additional_properties = d
        return trixel_map

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
