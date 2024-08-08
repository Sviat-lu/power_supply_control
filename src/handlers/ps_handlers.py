# This module manages the state of device channels, allowing for turning
# channels on/off and retrieving their current states.

from typing import Dict

from schemas import SourceOn
from .file_handlers import apply_changes, get_all_channels


async def source_on_ps(data: SourceOn) -> Dict:
    """
    Turn on a specified channel and update its voltage and current settings.
    
    Args:
        data (SourceOn): The data containing channel number, voltage, 
        and current.
    
    Returns:
        Dict: The updated state of specified channel.
    """
    all_channels: Dict = await get_all_channels()
    all_channels[data.channel] = {
        "output": "ON",
        "voltage": data.voltage,
        "current": data.current
    }

    await apply_changes(all_channels)
    return all_channels[data.channel]


async def source_off_ps(channel: str) -> Dict:
    """
    Turn off a specified channel.
    
    Args:
        channel (str): The channel number to be turned off.
    
    Returns:
        Dict: The updated state of the specified channel.
    """
    all_channels: Dict = await get_state_all_channels_ps()
    all_channels[channel]["output"] = "OFF"

    await apply_changes(all_channels)
    return all_channels[channel]


async def get_state_all_channels_ps() -> Dict:
    """
    Retrieve the current state of all channels.
    
    Returns:
        Dict: dictionary containing the states of all channels.
    """
    return await get_all_channels()


async def get_state_current_channel_ps(channel: int) -> Dict:
    """
    Retrieve the current state of a specific channel.
    
    Args:
        channel (int): The channel number to retrieve the state for.
    
    Returns:
        Dict: The state of the specified channel.
    """
    all_channels: Dict = await get_all_channels()
    return all_channels[channel]
