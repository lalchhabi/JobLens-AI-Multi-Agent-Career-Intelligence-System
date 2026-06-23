# Import libraries
from pydantic import BaseModel, Field

# Import project files
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.interview_schema import InterviewSchema
from schemas.gap_schema import GapSchema
from schemas.roadmap_schema import RoadmapSchema
from schemas.market_schema import MarketSchema


class CareerResponse(BaseModel):
    """
    Response schema for the complete career analysis workflow.
    """

    resume_analysis: ResumeSchema = Field(
        description="Structured insights extracted from the candidate's resume."
    )

    job_analysis: JobSchema = Field(
        description="Structured requirements and responsibilities extracted from the job description."
    )

    gap_analysis: GapSchema = Field(
        description="Comparison between candidate qualifications and job requirements."
    )

    interview_analysis: InterviewSchema = Field(
        description="Generated interview questions tailored to the candidate and target role."
    )

    learning_roadmap: RoadmapSchema = Field(
        description="Personalized recommendations and learning plan to address identified skill gaps."
    )

    market_analysis: MarketSchema = Field(
        description="Market intelligence and job recommendations."
    )