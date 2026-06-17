# Import libraries
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from services.career_analysis_service import CareerAnalysisService
import os, shutil, uuid, json
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import StreamingResponse
# Import project files
from utils.validators import validate_pdf, validate_job_description
from utils.logger import get_logger
from schemas.career_response_schema import CareerResponse
from utils.save_results import save_analysis
from fastapi.templating import Jinja2Templates

# Initialize module-level logger
logger = get_logger(__name__)

templates = Jinja2Templates(directory="ui/templates")


# Define routes
router = APIRouter()
service = CareerAnalysisService()
# Load templates file
BASE_DIR = Path(__file__).resolve().parent.parent



# Docs upload directory path
UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
       "index.html",
       {'request': request}
    )
        
@router.post("/analyze", response_model=CareerResponse)
async def analyze_career(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """Analyze resume and job description and return complete career report.

    Args:
        resume (UploadFile, optional): Resume of the employee. Defaults to File(...).
        job_description (UploadFile, optional): Job description. Defaults to File().
    """
    logger.info("Received career analysis request")

    #Validation layer
    resume = validate_pdf(resume)
    job_description = validate_job_description(job_description)
    logger.info(f"Resume uploaded: {resume.filename}")

    # Save file
    resume_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")

    resume.file.seek(0)
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    #service call
    try:
        logger.info("Starting career analysis service")
        result = service.career_analyze(
            resume_path= resume_path,
            job_description = job_description

        )
        logger.info("Career analysis completed successfully")
        save_path = save_analysis(result.model_dump())
        return result.model_dump()

    except Exception as e:
        logger.exception("Career Analysis Failed")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze_stream")
def analyze_stream(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
    ):
    """Execute the JobLens AI workflow using LangGraph streaming.

    Instead of waiting for the entire workflow to complete,
    this method yields intermediate node outputs as they
    become available.

    Workflow:
        Parser -> Resume Analysis -> Job Analysis ->
        Gap Analysis -> Interview Questions ->
        Learning Roadmap

    Args:
        resume_path (str):
            Path to the uploaded resume file.

        job_description (str):
            Raw job description text provided by the user.
            """
    def event_generator():
        # save file temporarily
        file_path = save_temp_file(resume)

        for event in service.career_analyze_stream(file_path, job_description):

            # convert to SSE format
            yield f"data: {json.dumps(event)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")