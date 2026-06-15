# Import libraries
from typing import TypedDict


# define state
class CareerState(TypedDict):
    resume_path: str
    job_description: str

    raw_resume: str
    raw_job_description: str

    resume_analysis: dict
    job_analysis: dict
    gap_analysis: dict
    interview_analysis: dict
    learning_roadmap: dict
