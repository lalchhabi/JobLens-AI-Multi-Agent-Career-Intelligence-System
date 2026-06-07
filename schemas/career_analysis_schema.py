# Import libraries
from pydantic import BaseModel

# Import schema files
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema
from schemas.interview_schema import InterviewSchema
from schemas.roadmap_schema import RoadmapSchema

# Schema for Career Analysis
class CareerAnalysisSchema(BaseModel):
    resume_analysis: ResumeSchema
    job_analysis: JobSchema
    gap_analysis: GapSchema
    interview_questions: InterviewSchema
    learning_roadmap: RoadmapSchema