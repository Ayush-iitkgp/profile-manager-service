import os
import logging
from fastapi import FastAPI
from src import settings
# from src.api.pnl_router import router as pnl_router
# from src.api.debug import router as debug_router
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
def hello():
    return {
        "message": "Hello World!"
    }


# app.include_router(pnl_router, prefix='/pnl')
# app.include_router(debug_router, prefix='/debug')

BASE_DIR = os.path.dirname(__file__)
