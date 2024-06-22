import os

from dotenv import load_dotenv

load_dotenv('.env')
API_BASE_URL = os.getenv('API_BASE_URL')
VERSION = os.getenv('VERSION')
NOTIFY_ALIVE_INTERVAL = int(os.getenv('NOTIFY_ALIVE_INTERVAL'))
NOME_ROBO = os.getenv('NOME_ROBO')
UUID_ROBO = os.getenv('UUID_ROBO')
API_AUTHORIZATION = os.getenv('API_AUTHORIZATION')
LOG_LEVEL = int(os.getenv('LOG_LEVEL'))
