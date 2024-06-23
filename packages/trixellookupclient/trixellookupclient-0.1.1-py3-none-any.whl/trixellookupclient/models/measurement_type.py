from enum import Enum

class MeasurementType(str, Enum):
    AMBIENT_TEMPERATURE = "ambient_temperature"
    RELATIVE_HUMIDITY = "relative_humidity"

    def __str__(self) -> str:
        return str(self.value)
