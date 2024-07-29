from typing import Callable

from fastapi import HTTPException, status

from src.config import MODE
from src.handlers.command_handlers import send_command


def mode_decorator(func: Callable):
    async def wrapper(command, **kwargs):
        if MODE == "test":
            return await func(command, **kwargs)
        elif MODE == "production":
            return await send_command(command)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Choose 'test' or 'production' mode in confg.py",
            )
    return wrapper
