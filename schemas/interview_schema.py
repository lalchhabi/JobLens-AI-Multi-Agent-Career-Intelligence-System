# Import libraries
from pydantic import BaseModel, Field
from typing import Optional, List

# Define Interview Information Schema
class Interview_schema(BaseModel):

    technical_questions: List[str] = Field(
        default_factory=list,
        description="List of the possible technical questions based on the job requirements and candidate skills"
    )

    behavioral_questions: List[str] = Field(
        default_factory=List,
        description="List of possible behavioral and situational interview questions"
    )

    project_based_questions: List[str] = Field(
        default_factory=list,
        description="List of questions related to project listed in the candidate's resume"
    )
