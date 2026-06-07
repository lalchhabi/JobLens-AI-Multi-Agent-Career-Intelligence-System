# Import libraries 
from typing import List, Optional
from pydantic import BaseModel, Field


# Learning Roadmap Schema here
class RoadmapSchema(BaseModel):
    first_week: List[str] = Field(
                            default_factory=list,
                            description="Learning tasks for Week 1")
    
    second_week: List[str] = Field(
                            default_factory=list,
                            description="Learning tasks for Week 2")
    
    projects: List[str] = Field(
                            default_factory=list,
                            description="Hands on project to build")
    
    resources: List[str] = Field(
                            default_factory=list,
                            description="Recommended learning resources")