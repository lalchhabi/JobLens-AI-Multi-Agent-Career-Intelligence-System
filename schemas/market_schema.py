#Import libraries
from pydantic import BaseModel, Field
from typing import List

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
        description="Most frequently requested skills across the retrieved live job listings."
    )

