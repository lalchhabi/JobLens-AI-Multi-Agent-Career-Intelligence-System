# Import libraries
from pydantic import BaseModel
from typing import List, Dict, Any

# Import schema files
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema
from schemas.interview_schema import InterviewSchema
from schemas.roadmap_schema import RoadmapSchema

# Schema for Career Analysis

class InterviewQuestions(BaseModel):
    technical_questions: List[str]
    behavioral_questions: List[str]
    project_based_questions: List[str]
    difficulty_level: str

class CareerAnalysisSchema(BaseModel):
    resume_analysis: Dict[str, Any]
    job_analysis: Dict[str, Any]
    gap_analysis: Dict[str, Any]
    interview_analysis: InterviewQuestions   
    learning_roadmap: Dict[str, Any]