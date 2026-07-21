#Import libraries
from pydantic import BaseModel, Field
from typing import List

class LiveJob(BaseModel):
    """A lightweight representation of a live job vacancy."""

    title: str = Field(
        description="Job title advertised by the employer."
    )

    company: str = Field(
        description="Company or organization hiring for the position."
    )

    location: str = Field(
        description="Job location including city, state, or country."
    )

    description: str = Field(
        description="A short summary of the job (80–150 characters) for quick preview."
    )

    apply_url: str = Field(
        description="Direct URL where the candidate can apply for the job."
    )

# Define market job schema
class MarketSchema(BaseModel):
    live_jobs: List[LiveJob] = Field(
        default_factory=list,
        description="Live job vacancies matching the candidate's target role."
    )
    similar_roles: List[str] = Field(
        default_factory = list,
        description = "Roles closely related to the target job")
    
    alternative_roles: List[str] = Field(
        default_factory = list,
        description = "Alternative career options matching candidate skills"
    )
    trending_skills: List[str] = Field(
        default_factory = list,
        description="Most frequently requested skills across the retrieved live job listings."
    )
    market_summary: str = Field(description = "Overall summary of market opportunities and hiring trends")
