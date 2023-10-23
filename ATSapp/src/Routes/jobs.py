from fastapi import APIRouter
from src.Utils.schemas import *
from src.Utils.helper import *

job_router = APIRouter()

@job_router.get("/{job_id}")
async def handle_job_details(job_id : str):
    pass


@job_router.get("/")
async def handle_all_jobs():
    pass

@job_router.post("/")
async def handle_submit_job(
    submitjobrequest: SubmitJobRequest
):
    job_description = submitjobrequest.job_description
    openai_instance = get_openaicaller_instance()
    resume_objects = openai_instance.get_relevant_resumes(
        job_description=job_description
        )
    print(resume_objects)
    return "sdfsf"