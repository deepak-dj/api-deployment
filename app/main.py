from fastapi import FastAPI
from .api import endpoints
from pydantic import BaseModel

apps = FastAPI()


# Include the images router


apps.include_router(endpoints.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(apps, host="0.0.0.0", port=8000)
