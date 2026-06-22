#Import libraries
from pydantic import BaseModel, Field
from typing import List

class JobRecommendation(BaseModel):
    title: str
    company: str
    location: str
    url: str



# Define market job schema
class MarketSchema(BaseModel):
    similar_roles: List[str] = Field(
        default_factory = list,
        description = "Roles closely related to the target job")
    
    alternative_roles: List[str] = Field(
        default_factory = list,
        description = "Alternative career options matching candidate skills"
    )
    trending_skills: List[str] = Field(
        default_factory = list,
        description = "Most demanded skills across current job market"
    )
    recommended_jobs: List[JobRecommendation] = Field(
        default_factory=list,
        description="Real job recommendations collected from job search"
    )
    market_summary: str = Field(description = "Overall summary of market opportunities and hiring trends")
