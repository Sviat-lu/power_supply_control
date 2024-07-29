from fastapi import APIRouter, status

from src.schemas import (
    AllChannelsResponse,
    CurrentChannelResponse,
    SourceOn,
    CurrentChannel,
)
from src.controller import (
    get_state_all_channels_command,
    get_state_current_channel_command,
    source_on_command,
    source_off_command,
)


router = APIRouter()


@router.post(
    "/source_on/",
    status_code=status.HTTP_200_OK,
    response_model=CurrentChannelResponse,
)
async def source_on(data: SourceOn):
    command = f"ADR {data.channel}:SOUR:CURR:IMM {data.current};"\
              f":ADR {data.channel}:SOUR:VOLT:IMM: {data.voltage};"\
              f":ADR {data.channel}:OUTP:IMM ON"
    return await source_on_command(command=command, data=data)


@router.post(
    "/source_off/",
    status_code=status.HTTP_200_OK,
    response_model=CurrentChannelResponse,
)
async def source_off(data: CurrentChannel):
    command = f":ADR {data.channel}:OUTP:IMM OFF"
    return await source_off_command(command=command, channel=data.channel)


@router.get(
    "/get_state_all/",
    status_code=status.HTTP_200_OK,
    response_model=AllChannelsResponse,
)
async def get_state_all_channels():
    command = "MEAS:ALL?"
    return await get_state_all_channels_command(command=command)


@router.post(
    "/get_state_current/",
    status_code=status.HTTP_200_OK,
    response_model=CurrentChannelResponse,
)
async def get_state_current_channel(data: CurrentChannel):
    command = "MEAS:ADR?"
    return await get_state_current_channel_command(
        command=command, channel=data.channel
    )
