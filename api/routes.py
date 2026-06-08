# Import libraries
from fastapi import APIRouter, UploadFile, File
from services.career_analysis_service import CareerAnalysisService

# Define routes
router = APIRouter()
service = CareerAnalysisService()

@router.post("/analyze")
async def analyze_career(
    resume: UploadFile = File(...),
    job_description: UploadFile = File()
):
    """Analyze resume and job description and return complete career report.

    Args:
        resume (UploadFile, optional): Resume of the employee. Defaults to File(...).
        job_description (UploadFile, optional): Job description. Defaults to File().
    """
    result = service.career_analyze(
        resume_path= resume.file,
        job_path = job_description.file

    )

    return result.model_dump()

