# import libraries
from pydantic import BaseModel, Field
from typing import List, Optional

# Define job schema
class JobSchema(BaseModel):
    title: Optional[str] = Field(default=None,
                                 description = "Title of the job")
    company: Optional[str] = Field(default=None,
                                   description="Hiring company name")

    required_skills: List[str] = Field(default_factory=list,
                                       description="Required skills for the role")
    preferred_skills: List[str] = Field(default_factory=list,
                                        description="Additional preferred skills but not mandatory")

    experience_level: Optional[str] = Field(default=None,
                                            description="Required experience level for the job")
    responsibilities: List[str] = Field(default_factory=list,
                                        description="List of duties and responsibilities")