# Import libraries
from pydantic import BaseModel, Field
from typing import List


# Define Gap Information Schema
class GapSchema(BaseModel):
    match_score: int = Field(description="Overall compatibility score between resume and job requirements")
    strong_skills: List[str] = Field(default_factory=list,
                                     description="Skills from the resume that strongly match the job requirements")
    
    missing_skills: List[str] = Field(default_factory=list,
                                       description="Required skills that are missing from the candidate's profile")
    
    learning_recommendation: List[str] = Field(default_factory=list,
                                               description="Suggested learning areas to improve job fit and close skill gaps")

