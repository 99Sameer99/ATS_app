from fastapi import FastAPI
from src.router import router
from src.MiddleWare import default_error_handler
from src.lifetime import *
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    ATSapp = FastAPI()
    register_start_event(app = ATSapp)
    register_shutdown_event(app = ATSapp)

    ATSapp.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    ATSapp.include_router(router)
    ATSapp.add_exception_handler(Exception, default_error_handler)
    return ATSapp