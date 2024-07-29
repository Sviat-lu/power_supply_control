import os
from typing import Dict

from fastapi import HTTPException, status


async def get_all_channels() -> Dict:
    await check_ps()
    with open("ps", "r") as ps:
        all_channels = ps.read()
    return eval(all_channels)


async def apply_changes(data: Dict) -> None:
    with open("ps", "w") as ps:
        data = str(data)
        ps.write(data)


async def check_ps() -> None:
    if os.path.exists("ps"):
        try:
            with open("ps", "r") as ip:
                file = ip.read()
            file = eval(file)
            if isinstance(file, Dict):
                return
        except (SyntaxError, NameError) as e:
            await create_ps()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"File corrupted: {e}"
            )
    else:
        await create_ps()


async def create_ps() -> None:
    default_state = {
        0: {"output": "OFF", "voltage": 0, "current": 0},
        1: {"output": "OFF", "voltage": 0, "current": 0},
        2: {"output": "OFF", "voltage": 0, "current": 0},
        3: {"output": "OFF", "voltage": 0, "current": 0}
    }
    with open("ps", "w") as ps:
        data = str(default_state)
        ps.write(data)
