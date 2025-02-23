from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import *

from services.settings import SettingsService


@asynccontextmanager
async def lifespan(app: FastAPI):
    await SettingsService.load()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(index.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, help="host", default="0.0.0.0")
    parser.add_argument("--port", type=int, help="port", default=8000)
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
