# Import libraries
from fastapi import UploadFile, HTTPException

def validate_pdf(file: UploadFile):
    """Validate the resume pdf file
    """
    if not file:
        raise HTTPException(status_code=400, detail="Resume file is required")
    
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    return file


def validate_job_description(text:str):
    """Validate the job description text
    """
    if not text or text.strip() == "":
        raise HTTPException(status_code=400, detail="Job Description cannot be empty")
    
    if len(text.strip()) < 30:
        raise HTTPException(status_code=400, detail="Job description is too short")
    
    return text.strip()

