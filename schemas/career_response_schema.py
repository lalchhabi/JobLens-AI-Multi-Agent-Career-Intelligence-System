# Import libraries
from pydantic import BaseModel, Field
from typing import Dict, Any, List


class CareerResponse(BaseModel):
    """
    Response schema for the complete career analysis workflow.
    """

    resume_analysis: Dict[str, Any] = Field(
        description="Structured insights extracted from the candidate's resume."
    )

    job_analysis: Dict[str, Any] = Field(
        description="Structured requirements and responsibilities extracted from the job description."
    )

    gap_analysis: Dict[str, Any] = Field(
        description="Comparison between candidate qualifications and job requirements."
    )

    interview_analysis: List[str] = Field(
        description="Generated interview questions tailored to the candidate and target role."
    )

    learning_roadmap: Dict[str, Any] = Field(
        description="Personalized recommendations and learning plan to address identified skill gaps."
    )