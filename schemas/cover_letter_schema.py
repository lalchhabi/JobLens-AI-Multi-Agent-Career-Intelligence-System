# Import required libraries
from pydantic import BaseModel, Field
from typing import List

class CoverLetterSchema(BaseModel):
    """Schema for generated job application content."""

    full_cover_letter: str = Field(
        description="A personalized, complete cover letter tailored to the candidate's resume and the target job."
    )

    application_email: str = Field(
        description="A concise professional email for submitting the job application."
    )

    linkedin_message: str = Field(
        description="A short personalized LinkedIn message for connecting with the recruiter or hiring manager."
    )
