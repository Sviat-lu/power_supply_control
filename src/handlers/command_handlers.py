import socket

from fastapi import HTTPException, status

from src.config import IP, PORT


async def send_command(command: str) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, PORT))
            s.sendall(command.encode('ascii'))
            response = s.recv(1024).decode()
            return response
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Connected device not found",
        )
