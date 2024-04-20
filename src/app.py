import os
import logging
from fastapi import FastAPI
from src import settings
from src.api.customer import router as customer_router
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    docs_url='/docs',
    redoc_url='/redoc',
)


@app.on_event('startup')
async def startup():
    logger.info("startup: Starting the app")


@app.get("/")
async def debug():
    return "profile-manager-service is working"


app.include_router(customer_router, prefix='/v1/customer')

BASE_DIR = os.path.dirname(__file__)