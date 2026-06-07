# Import project file
from tools.pdf_parser import PDFparser

from agents.resume_agent import ResumeAgent
from agents.job_agent import JobAgent
from agents.gap_agent import GapAnalysisAgent
from agents.interview_agent import InterviewAgent
from agents.roadmap_agent import RoadmapAgent

from schemas.career_analysis_schema import CareerAnalysisSchema

class CareerAnalysisService():
    """
    Orchestrates the full AI career pipeline

    Resume -> Job -> Gap -> Interview -> Roadmap

    This is the core business logic layer of the system.
    """

    def __init__(self):
        # Tools
        self.parser = PDFparser()

        #Agents
        self.resume_agent = ResumeAgent()
        self.job_agent = JobAgent()
        self.gap_agent = GapAnalysisAgent()
        self.interview_agent = InterviewAgent()
        self.roadmap_agent = RoadmapAgent()

    def career_analyze(self,
                       resume_path: str,
                       job_path: str
                    ) -> CareerAnalysisSchema:
        """Run full Career Intelligent Pipeline

        Args:
            resume_path (str): Path to resume pdf
            job_path (str): path to job description pdf

        Returns:
            CareerAnalysisSchema: Complete AI analysis result
        """

        # Step 1: Extract text
        raw_resume = self.parser.extract_text(resume_path)
        raw_job = self.parser.extract_text(job_path)

        # Step 2: Structured Parsing
        resume_data = self.resume_agent.parse_resume(raw_resume)
        job_data = self.job_agent.analyze_job(raw_job)

        # Step 3: Gap Analysis
        gap_data = self.gap_agent.gap_analyze(resume_data, job_data)

        # Step 4: Interview Questions
        interview_data = self.interview_agent.generate_interview_questions(
            project_info=resume_data,
            job_description=job_data,
            learning_recommend=gap_data,
            difficult_level='medium'
        )

        # Step 5: Roadmap Generation
        roadmap_data = self.roadmap_agent.generate_roadmap(
            gap_data=gap_data,
            job_data=job_data
        )

        # Step 6: Combine Results
        return CareerAnalysisSchema(
            resume_analysis=resume_data,
            job_analysis=job_data,
            gap_analysis=gap_data,
            interview_questions=interview_data,
            learning_roadmap=roadmap_data
        )