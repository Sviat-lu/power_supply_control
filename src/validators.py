from typing import Dict, Union
from fastapi.exceptions import RequestValidationError

ACCEPTED_START_COMMANDS = ("min", "minimum", "max", "maximum")


def validate_channel(field: int) -> int:
    if isinstance(field, int) and field < 0 or field > 3:
        raise RequestValidationError("Choose channel in range 0~3")
    return field


def validate_voltage(field: Union[float, str]) -> Union[float, str]:
    if isinstance(field, float) and (field < 0 or field > 10):
        raise RequestValidationError("Choose voltage in range 0~10(V)")
    elif (
        isinstance(field, str)
        and field.lower() not in ACCEPTED_START_COMMANDS
    ):
        raise RequestValidationError(
            "Integers, floats and min/max available"
        )
    return field


def validate_current(field: Union[float, str]) -> Union[float, str]:
    if isinstance(field, float) and (field < 0 or field > 5):
        raise RequestValidationError("Choose current in range 0~5(A)")
    elif (
        isinstance(field, str)
        and field.lower() not in ACCEPTED_START_COMMANDS
    ):
        raise RequestValidationError(
            "Integers, floats and min/max available"
        )
    return field


def prepare_all_channels_response_data(data: Dict) -> Dict:
    all_channels_dict = {}
    all_channels_list = []
    for k, v in data.items():
        channel = {
            "channel": k,
            "output": v["output"],
            "voltage": v["voltage"],
            "current": v["current"],
        }
        all_channels_list.append(channel)
    all_channels_dict["all_channels"] = all_channels_list
    return all_channels_dict
