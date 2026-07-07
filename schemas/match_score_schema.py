# Import required libraries
from pydantic import BaseModel, Field

class MatchScoreSchema(BaseModel):
    """Structured output for deterministic match score calculation."""

    overall_score: int = Field(
        description="Overall resume-job compatibility score (0-100)"
    )

    required_skill_score: int = Field(
        description="Percentage of required skills matched"
    )

    preferred_skill_score: int = Field(
        description="Percentage of preferred skills matched"
    )

    matched_required: int = Field(
        description="Number of required skills matched"
    )

    total_required: int = Field(
        description="Total number of required skills"
    )

    matched_preferred: int = Field(
        description="Number of preferred skills matched"
    )

    total_preferred: int = Field(
        description="Total number of preferred skills"
    )