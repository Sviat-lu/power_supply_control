from typing import Dict, List, Union
from pydantic import BaseModel, field_validator, model_validator

from .validators import (
    prepare_all_channels_response_data,
    validate_channel,
    validate_voltage,
    validate_current,
)


class SourceBase(BaseModel):
    channel: int

    @field_validator("channel")
    def channel_validator(channel: int) -> int:
        return validate_channel(channel)


class CurrentChannel(SourceBase):
    ...


class SourceOn(SourceBase):
    voltage: Union[float, str]
    current: Union[float, str]

    @field_validator("voltage")
    def voltage_validator(voltage: Union[float, str]) -> Union[float, str]:
        return validate_voltage(voltage)

    @field_validator("current")
    def current_validator(current: Union[float, str]) -> Union[float, str]:
        return validate_current(current)


class CurrentChannelResponse(BaseModel):
    output: str = ("ON" or "OFF")
    voltage: int
    current: int
    power: int

    @model_validator(mode="before")
    def calculate_power(self: Dict) -> Dict:
        self["power"] = self["voltage"] * self["current"]
        return self


class CurrentChannelResponseInAll(CurrentChannelResponse):
    channel: int


class AllChannelsResponse(BaseModel):
    all_channels: List[CurrentChannelResponseInAll]

    @model_validator(mode="before")
    def all_channels_validator(self: Dict) -> Dict:
        return prepare_all_channels_response_data(self)
