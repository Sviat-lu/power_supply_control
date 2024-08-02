# This module handles the management of device channels, including reading from a file,
# applying changes, and resetting to default settings if necessary.

from typing import Dict
import os
from fastapi import HTTPException, status
import logging

logger = logging.getLogger(__name__)

async def get_all_channels() -> Dict:
    """
    Retrieve all channels from the device configuration file.
    
    Returns:
        Dict: A dictionary containing all channel configurations.
    """
    all_channels: Dict = await read_file()
    return all_channels


async def read_file() -> Dict:
    """
    Read the device configuration from a file.
    
    Returns:
        Dict: A dictionary containing the device's channel configurations.
    
    Raises:
        HTTPException: If the firmware is corrupted and cannot be read.
    """
    if os.path.exists("ps"):
        try:
            with open("ps", "r") as ps:
                all_channels = ps.read()
            logger.info("Device successfully detected")
            file: Dict = eval(str(all_channels))
            if isinstance(file, Dict):
                logger.info("Connection established successfully")
                return file
        except (SyntaxError, NameError):
            err = "Device firmware is corrupted. Resetting to default settings"
            logger.error(err)
            await create_ps()
            logger.info("The device has been reset to factory settings.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err
            )
    else:
        await create_ps()  


async def apply_changes(data: Dict) -> None:
    """
    Apply changes to the device configuration by writing to the file.
    
    Args:
        data (Dict): The new configuration data to be written.
    """
    with open("ps", "w") as ps:
        data = str(data)
        ps.write(data)


async def create_ps() -> None:
    """
    Create a default device configuration and save it to file.
    """
    default_state = {
        0: {"output": "OFF", "voltage": 0, "current": 0},
        1: {"output": "OFF", "voltage": 0, "current": 0},
        2: {"output": "OFF", "voltage": 0, "current": 0},
        3: {"output": "OFF", "voltage": 0, "current": 0}
    }
    await apply_changes(str(default_state))
