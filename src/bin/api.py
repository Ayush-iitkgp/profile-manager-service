import uvicorn

from src import settings

if __name__ == "__main__":
    uvicorn.run(app="src.app:app", host=settings.HOST, port=settings.PORT)
