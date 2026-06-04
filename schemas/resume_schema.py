# Import libraries
from pydantic import BaseModel, Field
from typing import List, Optional


# Project Information Schema
class Project(BaseModel):
    name: str = Field(description="Name of the project")

    
    description: Optional[str] = Field(default = None,description="Description of the project")

    
    tech_stack: List[str] = Field(default_factory=list, description = 'Technologies used in the project')


# Work Experience Schema
class Experience(BaseModel):
    company: str = Field(description = "Name of the company")

    role: str = Field(description = "Job title")

    duration: Optional[str] = Field(default = None, description = "Duration of the job")

    responsibilities: List[str] = Field(default_factory=list, description = "Key responsibilities or achievements")


# Education Schema
class Education(BaseModel):
    
    institution: str = Field(description = "Institution name")

    
    degree: Optional[str] = Field(default = None,
                                  description = "Degree obtained")

    year: Optional[str] = Field(default = None,
                                description = "# Graduation year")


# Main Resume Schema
class ResumeSchema(BaseModel):
    name: Optional[str] = Field(
        default = None,
        description = "Candidate name"
    )

    email: Optional[str] = Field(
        default = None,
        description = "Candidate email address"
    )

    
    skills: List[str] = Field(default_factory=list,
                              description = "Technical and professional skills")

    projects: List[Project] = Field(default_factory=list,
                                    description = " Projects completed by candidate")

    experience: List[Experience] = Field(default_factory=list, description = "Professional experience history")

    education: List[Education] = Field(default_factory=list,
                                       description = "Educational qualifications")