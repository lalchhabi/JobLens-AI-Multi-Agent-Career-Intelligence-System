# Import libraries
from pydantic import BaseModel
from typing import List, Dict, Any

# Import schema files
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema
from schemas.interview_schema import InterviewSchema
from schemas.roadmap_schema import RoadmapSchema
from schemas.market_schema import MarketSchema

# Schema for Career Analysis

class InterviewQuestions(BaseModel):
    technical_questions: List[str]
    behavioral_questions: List[str]
    project_based_questions: List[str]
    difficulty_level: str

class CareerAnalysisSchema(BaseModel):
    """
    Aggregated output of the JobLens multi-agent career analysis pipeline.
    """
    resume_analysis: ResumeSchema
    job_analysis: JobSchema
    gap_analysis: GapSchema
    interview_analysis: InterviewSchema
    learning_roadmap: RoadmapSchema
    market_analysis: MarketSchema