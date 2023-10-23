from dataclasses import dataclass
from pydantic import BaseModel
from typing import List, Dict


# request schemas
class SubmitJobRequest(BaseModel):
    job_description: str

# db schemas
@dataclass
class JobPost:
    job_description: str
    submit_timestamp: float
    status: str
    shortlisted_resumes: List[str]
    score: List[str]
    company_name: str
    role: str