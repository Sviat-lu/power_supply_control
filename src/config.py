import os
from dotenv import load_dotenv

load_dotenv(override=True)


IP = os.getenv('IP')
PORT = os.getenv('PORT')
MODE = os.getenv('MODE')
