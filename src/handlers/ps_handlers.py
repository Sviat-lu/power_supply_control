from typing import Dict

from src.schemas import SourceOn
from .file_helpers import apply_changes, get_all_channels


async def source_on_ps(data: SourceOn) -> Dict:
    all_channels = await get_all_channels()
    all_channels[data.channel] = {
        "output": "ON",
        "voltage": data.voltage,
        "current": data.current
    }

    await apply_changes(all_channels)
    return all_channels[data.channel]


async def source_off_ps(channel: str) -> Dict:
    all_channels = await get_state_all_channels_ps()
    all_channels[channel]["output"] = "OFF"

    await apply_changes(all_channels)
    return all_channels[channel]


async def get_state_all_channels_ps() -> Dict:
    return await get_all_channels()


async def get_state_current_channel_ps(channel: int) -> Dict:
    all_channels = await get_all_channels()
    return all_channels[channel]
