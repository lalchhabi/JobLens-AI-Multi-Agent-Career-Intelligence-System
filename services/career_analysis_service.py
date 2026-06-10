# Import project file
from tools.pdf_parser import PDFparser

from agents.resume_agent import ResumeAgent
from agents.job_agent import JobAgent
from agents.gap_agent import GapAnalysisAgent
from agents.interview_agent import InterviewAgent
from agents.roadmap_agent import RoadmapAgent

from schemas.career_analysis_schema import CareerAnalysisSchema
from utils.logger import get_logger

# Initialize module-level logger
logger = get_logger(__name__)

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
                       job_description: str
                    ) -> CareerAnalysisSchema:
        """Run full Career Intelligent Pipeline

        Args:
            resume_path (str): Path to resume pdf
            job_description (str): Job description 

        Returns:
            CareerAnalysisSchema: Complete AI analysis result
        """
        try:
            # Step 1: Extract text
            logger.info("Extracting resume text")
            raw_resume = self.parser.extract_text(resume_path)
            raw_job = job_description

            # Step 2: Structured Parsing
            logger.info("Running Resume Agent")
            resume_data = self.resume_agent.parse_resume(raw_resume)
            logger.info("Running Job Analysis Agent")
            job_data = self.job_agent.analyze_job(raw_job)

            # Step 3: Gap Analysis
            logger.info("Running Gap Analysis Agent")
            gap_data = self.gap_agent.gap_analyze(resume_data, job_data)

            # Step 4: Interview Questions
            logger.info("Running Interview Agent")
            interview_data = self.interview_agent.generate_interview_questions(
                project_info=resume_data,
                job_description=job_data,
                learning_recommend=gap_data,
                difficult_level='medium'
            )

            # Step 5: Roadmap Generation
            logger.info("Running Learning Roadmap Agent")
            roadmap_data = self.roadmap_agent.generate_roadmap(
                gap_data=gap_data,
                job_data=job_data
            )
            logger.info("Career analysis pipeline completed")

            # Step 6: Combine Results
            return CareerAnalysisSchema(
                resume_analysis=resume_data,
                job_analysis=job_data,
                gap_analysis=gap_data,
                interview_analysis=interview_data,
                learning_roadmap=roadmap_data
            )
        except Exception as e:
            logger.error(f"Career analysis failed: {str(e)}")
            raise 