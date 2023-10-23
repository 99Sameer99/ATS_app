from fastapi import APIRouter
from src.Routes.upload import upload_router
from src.Routes.jobs import job_router

router = APIRouter()


@router.get("/")
async def index():
    return "App is alive"


router.include_router(
    router= upload_router,
    prefix = "/upload",
    tags= ["upload"]
)


router.include_router(
    router= job_router,
    prefix = "/jobs",
    tags = ["jobs"]
)