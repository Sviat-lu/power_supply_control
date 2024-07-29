from typing import Dict

from src.decorators import mode_decorator
from .handlers.ps_handlers import (
    get_state_all_channels_ps,
    get_state_current_channel_ps,
    source_off_ps,
    source_on_ps,
)
from src.logger import logger
from src.schemas import SourceOn


@mode_decorator
async def source_on_command(command: str, data: SourceOn) -> Dict:
    logger.info(f"Command recieved: {command}")
    result = await source_on_ps(data)
    logger.info(f"Result data: {result}")
    return result


@mode_decorator
async def source_off_command(command: str, channel: str) -> Dict:
    logger.info(f"Command recieved: {command}")
    result = await source_off_ps(channel)
    logger.info(f"Result data: {result}",)
    return result


@mode_decorator
async def get_state_all_channels_command(command: str) -> Dict:
    logger.info(f"Command recieved: {command}")
    result = await get_state_all_channels_ps()
    logger.info(f"Result data: {result}")
    return result


@mode_decorator
async def get_state_current_channel_command(
    command: str, channel: int
) -> Dict:
    logger.info(f"Command recieved: {command}")
    result = await get_state_current_channel_ps(channel)
    logger.info(f"Result data: {result}")
    return result
