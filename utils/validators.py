# Import libraries
from fastapi import UploadFile, HTTPException

# Keep in sync with MAX_RESUME_BYTES in ui/static/js/app.js and with the
# limit advertised on the upload card in ui/templates/index.html
MAX_RESUME_BYTES = 5 * 1024 * 1024


def validate_pdf(file: UploadFile):
    """Validate the resume pdf file
    """
    if not file:
        raise HTTPException(status_code=400, detail="Resume file is required")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    if file.size is not None and file.size > MAX_RESUME_BYTES:
        limit_mb = MAX_RESUME_BYTES // (1024 * 1024)
        raise HTTPException(
            status_code=413,
            detail=f"Resume is too large. The maximum size is {limit_mb} MB."
        )

    return file


def validate_job_description(text:str):
    """Validate the job description text
    """
    if not text or text.strip() == "":
        raise HTTPException(status_code=400, detail="Job Description cannot be empty")
    
    if len(text.strip()) < 30:
        raise HTTPException(status_code=400, detail="Job description is too short")
    
    return text.strip()

