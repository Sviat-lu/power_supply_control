# Function to send a command to a device over a TCP socket

import socket

from fastapi import HTTPException, status

from config import IP, PORT
from utils import logger


def send_command(command: str) -> str:
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect the socket to the server's address and port
            s.connect((IP, PORT))
            logger.info("Device successfully connected")

            # Send the command to the device, encoding it in ASCII
            s.sendall(command.encode('ascii'))

            # Receive the response from the device, decoding it back to string
            response = s.recv(1024).decode
            return response
            
    except Exception:
        logger.error("Connected device not found")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Connected device not found",
        )
