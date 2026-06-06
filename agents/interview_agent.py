# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from prompts.interview_prompt import INTERVIEW_PROMPT
from schemas.interview_schema import InterviewSchema
from services.llm_service import get_llm_model
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema

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

        # Build final prompt
        prompt = INTERVIEW_PROMPT.format(
            resume_projects = project_info.model_dump_json(indent=2),
            job_description = job_description.model_dump_json(indent=2),
            learning_recommendations = learning_recommend.model_dump_json(indent=2),
            difficulty_level = difficult_level,
            format_instructions = self.parser.get_format_instructions()
        )

        # Call the LLM model to generate interview questions
        response = self.llm_model.invoke(prompt)

        # Convert raw result into structured format 
        result = self.parser.parse(response.content)

        return result