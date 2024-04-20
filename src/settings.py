from os import getenv

TITLE = "Profile Manager Service for password and language setup"
DESCRIPTION = "This services allows you to manage your password and language profiles."

PORT = int(getenv("APP_PORT", "3000"))
HOST = getenv("APP_HOST")

DATABASE_URL = getenv("DATABASE_URL")
DATABASE_NAME = getenv("DATABASE_NAME")
DATABASE_POOL_SIZE = int(getenv("DATABASE_POOL_SIZE"))
REQUIRED_VERSION = getenv("REQUIRED_VERSION", "2.1.0")
SECRET_KEY = getenv("SECRET_KEY")
