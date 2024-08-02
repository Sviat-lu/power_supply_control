import logging


file_format = logging.Formatter(
    fmt="{levelname} | {asctime} | {module} | {funcName} | {message}",
    style="{",
)
stream_format = logging.Formatter(fmt="{levelname} | {message}", style="{")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename="api.log", mode="a")
file_handler.setFormatter(file_format)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_format)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
