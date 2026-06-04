# import libraries
from pydantic import BaseModel, Field
from typing import List, Optional

# Define job schema
class JobSchema(BaseModel):
    # title of the job
    title: Optional[str] = Field(description = [])
    company: Optional[str] = None

    required_skills: List[str] = []
    preferred_skills: List[str] = []

    experience_level: Optional[str] = None
    responsibilities: List[str] = []