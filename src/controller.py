# This module defines commands for managing the state of device channels.
# Each command is decorated with a mode_decorator for for additional
# functionality of determining the program's operating mode.
# The commands include turning channels on/off and retrieving their states.

from typing import Dict

from .decorators import mode_decorator
from .handlers.ps_handlers import (
    get_state_all_channels_ps,
    get_state_current_channel_ps,
    source_off_ps,
    source_on_ps,
)
from .loggers import logger
from .schemas import SourceOn


@mode_decorator
async def source_on_command(command: str, data: SourceOn) -> Dict:
    """
    Command to turn on a specified channel.
    
    Args:
        command (str): The command string received.
        data (SourceOn): The data containing channel number, voltage, 
        and current.
    
    Returns:
        Dict: The updated state of the specified channel.
    """
    logger.info(f"Command recieved: {command}")
    result: Dict = await source_on_ps(data)
    logger.info(
        f"Channel {data.channel} enabled. "
        f"Voltage: {result["voltage"]}, current: {result["current"]}"
    )
    return result


@mode_decorator
async def source_off_command(command: str, channel: str) -> Dict:
    """
    Command to turn off a specified channel.
    
    Args:
        command (str): The command string received.
        channel (str): The channel number to be turned off.
    
    Returns:
        Dict: The updated state of the specified channel.
    """
    logger.info(f"Command recieved: {command}")
    result: Dict = await source_off_ps(channel)
    logger.info(
        f"Channel {channel} disabled. "
        f"Voltage: {result["voltage"]}, current: {result["current"]}"
    )
    return result


@mode_decorator
async def get_state_all_channels_command(command: str) -> Dict:
    """
    Command to retrieve the state of all channels.
    
    Args:
        command (str): The command string received.
    
    Returns:
        Dict: A dictionary containing the states of all channels.
    """
    logger.info(f"Command recieved: {command}")
    result: Dict = await get_state_all_channels_ps()

    for k, v in result.items():
        logger.info(f"Channel: {k}, output: {v["output"]}, "
                    f"voltage: {v["voltage"]}, current: {v["current"]}")

    return result


@mode_decorator
async def get_state_current_channel_command(
    command: str, channel: int
) -> Dict:
    """
    Command to retrieve the state of a specific channel.
    
    Args:
        command (str): The command string received.
        (int): The channel number to retrieve the state for.
    
    Returns:
        Dict: The state of the specified channel.
    """
    logger.info(f"Command recieved: {command}")
    result: Dict = await get_state_current_channel_ps(channel)
    logger.info(
        f"Channel {channel} status is {result["output"]}. "
        f"Voltage: {result["voltage"]}, current: {result["current"]}"
    )
    return result
