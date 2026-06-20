#Import libraries
from pydantic import BaseModel, Field
from typing import Field, Literal, List

# Define market job schema
class RecommendedRole(BaseModel):
    title: str = Field(descriptipn = "Recommended Job title")
    match_score: str = Field(description = "Job Match Score")


class MarketSchema(BaseModel):
    recommended_roles: List[RecommendedRole] = Field(description = "Recommended Job Role")
    trending_skills: List[str] = Field(default_factory = list, description = "Trending job skills")
    career_advice: str = Field(description = "Career_advice")
