#Import libraries
from pydantic import BaseModel, Field
from typing import List

class JobRecommendation(BaseModel):
    title: str
    url: str
    company: str | None = None
    location: str | None = None


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
    market_summary: str = Field(description = "Overall summary of market opportunities and hiring trends")
