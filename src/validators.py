from typing import Dict, Union
from fastapi.exceptions import RequestValidationError

from .loggers import logger

ACCEPTED_START_COMMANDS = ("min", "minimum", "max", "maximum")


def validate_channel(field: int) -> int:
    """
    Validates the channel number to ensure it is within the acceptable range (0-3).
    
    Raises a RequestValidationError if the channel is out of range.
    """
    if isinstance(field, int) and field < 0 or field > 3:
        logger.warning("Channel out of range")
        raise RequestValidationError("Choose channel in range 0~3")
    return field


def voltage_and_current_validator(
    field: Union[float, str], max_value: int, err_message: str
) -> Union[float, str]:
    """
    Validates voltage and current values to ensure they are within the specified range.
    
    Accepts both float values and specific string commands. 
    Raises a RequestValidationError if invalid.
    """
    if isinstance(field, float) and (field < 0 or field > max_value):
        logger.warning("Value out of range")
        raise RequestValidationError(err_message)
    elif (
        isinstance(field, str)
        and field.lower() not in ACCEPTED_START_COMMANDS
    ):
        logger.warning("Incorrect current value")
        raise RequestValidationError(
            "Integers, floats and min/max available"
        )
    return field


def prepare_all_channels_response_data(data: Dict) -> Dict:
    """
    Prepares the response data for all channels by formatting it into a list of dictionaries.
    
    Each dictionary contains channel information including output, voltage, and current.
    """
    all_channels_list = []
    for k, v in data.items():
        channel = {
            "channel": k,
            "output": v["output"],
            "voltage": v["voltage"],
            "current": v["current"],
        }
        all_channels_list.append(channel)
    return {"all_channels": all_channels_list}
