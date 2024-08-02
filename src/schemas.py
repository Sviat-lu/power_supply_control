from typing import Dict, List, Union
from pydantic import BaseModel, field_validator, model_validator

from .validators import (
    prepare_all_channels_response_data,
    validate_channel,
    voltage_and_current_validator,
)


# Base model for source channels, inheriting from Pydantic's BaseModel
class SourceBase(BaseModel):
    channel: int

    @field_validator("channel")
    def channel_validator(channel: int) -> int:
        return validate_channel(channel)


# Model for current channel model, inheriting from SourceBase
class CurrentChannel(SourceBase):
    ...


# Model for turning on a source, inheriting from SourceBase
class SourceOn(SourceBase):
    voltage: Union[float, str]
    current: Union[float, str]

    @field_validator("voltage")
    def voltage_validator(voltage: Union[float, str]) -> Union[float, str]:
        err_message = "Choose voltage in range 0~10(V)"
        return voltage_and_current_validator(
            voltage, max_value=10, err_message=err_message
        )

    @field_validator("current")
    def current_validator(current: Union[float, str]) -> Union[float, str]:
        err_message = "Choose current in range 0~5(A)"
        return voltage_and_current_validator(
            current, max_value=5, err_message=err_message
        )


# Model for the response of a current channel
class CurrentChannelResponse(BaseModel):
    output: str = ("ON" or "OFF")
    voltage: int
    current: int
    power: int

    @model_validator(mode="before")
    def calculate_power(data: Dict) -> Dict:
        data["power"] = data["voltage"] * data["current"]
        return data


# Model for the response of a current channel number in AllChannelsResponse
class CurrentChannelResponseInAll(CurrentChannelResponse):
    channel: int


# Model for the response containing all channels
class AllChannelsResponse(BaseModel):
    all_channels: List[CurrentChannelResponseInAll]

    @model_validator(mode="before")
    def all_channels_validator(data: Dict) -> Dict:
        return prepare_all_channels_response_data(data)
