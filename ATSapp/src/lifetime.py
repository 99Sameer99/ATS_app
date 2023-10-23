from typing import Awaitable, Callable
from fastapi import FastAPI
from src.Utils.helper import *
from src.Utils.config import Config


def register_start_event(app: FastAPI) -> Callable[[], Awaitable[None]]:
    @app.on_event("startup")
    async def _startup():
        print("[INFO] Creating resume directory")
        await create_dir(Config.RESUME_DIR)
    return _startup
        
def register_shutdown_event(app: FastAPI) -> Callable[[], Awaitable[None]]:
    @app.on_event("shutdown")
    async def _shutdown():
        print("[INFO] Deleting resume directory")
        #await delete_dir(Config.RESUME_DIR)
    return _shutdown