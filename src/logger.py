import logging


logger = logging.getLogger("lol")

logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="{levelname}|{asctime}|{message}",
    style="{",
    filemode="a",
)
