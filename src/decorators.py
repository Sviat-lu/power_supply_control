from typing import Callable

from fastapi import HTTPException, status

from config import MODE
from handlers import send_command
from utils import logger


def mode_decorator(func: Callable):
    """
    A decorator to handle different operating modes (test and production).

    This decorator checks the current mode and decides whether to execute the
    original function or to send a command directly. It raises an if 
    the mode is incorrect.
    """
    async def mode_definition(command, **kwargs):
        if MODE == "test":
            logger.info("Test mode enabled")
            return await func(command, **kwargs)
        elif MODE == "production":
            logger.info("Production mode enabled")
            return send_command(command)
        else:
            logger.error("Incorrect operating mode selected")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Choose 'test' or 'production' mode in confg.py",
            )
    return mode_definition
