# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from prompts.interview_prompt import INTERVIEW_PROMPT
from schemas.interview_schema import InterviewSchema
from services.llm_service import get_llm_model
from utils.llm_retry import safe_llm_call
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema
from utils.logger import get_logger
from services.context_builder import build_interview_context


# Define logger
logger = get_logger(__name__)

class InterviewAgent:
    """
    Generates interview questions based on:

    - Candidate projects
    - Job requirements
    - Skill gap analysis

    The agent produces structured interview questions
    categorized into:
    - Behavioral questions
    - Technical questions
    - Project-based questions
    """
    def __init__(self):
        
        # Initialize LLM model
        self.llm_model = get_llm_model()
        self.agent_name = "Interview Agent"

        # Define pydantic parser to get structured output
        self.parser = PydanticOutputParser(pydantic_object=InterviewSchema)

    def generate_interview_questions(
        self, 
        project_info:ResumeSchema, 
        job_description:JobSchema, 
        learning_recommend:GapSchema, 
        difficult_level:str
    )-> InterviewSchema:
        """
        Generate interview questions tailored to the candidate.

        Args:
            project_info (ResumeSchema):
                Parsed resume data containing projects, skills, etc.

            job_description (JobSchema):
                Structured job requirements.

            learning_recommend (GapSchema):
                Gap analysis output containing missing skills and recommendations.

            difficulty_level (str):
                Difficulty level of questions (easy, medium, hard).

        Returns:
            InterviewSchema:
                Structured interview questions categorized into:
                - behavioral_questions
                - technical_questions
                - project_questions
        """

        format_instructions = self.parser.get_format_instructions()
        
        resume_detail = ResumeSchema(**project_info)
        job_detail = JobSchema(**job_description)
        gap_detail = GapSchema(**learning_recommend)


        interview_context = build_interview_context(
            resume_detail,
            job_detail,
            gap_detail,
        )

        # Build final prompt
        prompt = INTERVIEW_PROMPT.format(
            interview_context=interview_context,
            difficulty_level=difficult_level,
            format_instructions=format_instructions,
        )

        logger.info("Interview Agent Prompt Profile")
        logger.info(f"Interview Agent Prompt          : {len(prompt)}")

        # Call the LLM model to generate interview questions
        response = safe_llm_call(
            lambda: self.llm_model.invoke(prompt),
            prompt=prompt,
            agent_name=self.agent_name,
        )

        # Convert raw result into structured format 
        result = self.parser.parse(response.content)

        return result