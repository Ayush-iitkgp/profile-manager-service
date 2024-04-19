from os import getenv

TITLE = "FastAPI Python Service"
DESCRIPTION = "Lighting fast Python API"

PORT = int(getenv('APP_PORT', '3000'))
HOST = getenv('APP_HOST')

DATABASE_URL = getenv('DATABASE_URL')
DATABASE_NAME = getenv('DATABASE_NAME')
DATABASE_POOL_SIZE = int(getenv('DATABASE_POOL_SIZE'))