# Import libraries
from pydantic import BaseModel, Field
from typing import List
from schemas.match_score_schema import MatchScoreSchema


# Define Gap Information Schema
class GapSchema(BaseModel):
    matched_required_skills: List[str] = Field(default_factory=list,
                                         description="Skills required for the job that are present in the candidate's resume")
    
    missing_required_skills: List[str] = Field(default_factory=list,
                                         description="Skills required for the job that are missing from the candidate's resume")
    
    matched_preferred_skills: List[str] = Field(default_factory=list,
                                         description="Preferred skills for the job that are present in the candidate's resume")
    
    missing_preferred_skills: List[str] = Field(
                                        default_factory=list,
                                        description="Skills that are preferred for the job that are missing from candidate's resume"
    )
    
    learning_recommendation: List[str] = Field(default_factory=list,
                                               description="Suggested learning areas to improve job fit and close skill gaps")

    match_score: MatchScoreSchema | None = None


class GapLLMSchema(BaseModel):
    matched_required_skills: List[str] = Field(
        default_factory=list,
        description="Required skills found in resume."
    )

    missing_required_skills: List[str] = Field(
        default_factory=list,
        description="Required skills missing from resume."
    )

    matched_preferred_skills: List[str] = Field(
        default_factory=list,
        description="Preferred skills found in resume."
    )

    missing_preferred_skills: List[str] = Field(
        default_factory=list,
        description="Preferred skills missing from resume."
    )

    learning_recommendation: List[str] = Field(
        default_factory=list,
        description="Learning recommendations."
    )