# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from prompts.gap_prompt import GAP_PROMPT
from schemas.gap_schema import GapSchema
from services.llm_service import get_llm_model
from utils.llm_retry import safe_llm_call


# Gap Analysis Agent
class GapAnalysisAgent:
    """
    GapAnalysisAgent compares a candidate's resume with a job description
    and generates a structured gap analysis report using an LLM.

    Responsibilities:
    - Semantic skill matching
    - Match score calculation (via LLM)
    - Identify strong & missing skills
    - Generate learning recommendations
    """

    def __init__(self):

        # Initialize LLM model
        self.llm = get_llm_model()

        # Pydantic parser ensures structured output (GapSchema validation)
        self.parser = PydanticOutputParser(pydantic_object=GapSchema)

    def gap_analyze(self, resume_detail:str, job_description:str)-> GapSchema:
        """
        Perform gap analysis between resume and job description.

        Args:
            resume_data (str): Structured or raw resume text/data
            job_data (str): Job description text

        Returns:
            GapSchema: Structured gap analysis result
        """

        #Build final prompt
        prompt = GAP_PROMPT.format(
            resume_data = resume_detail, 
            job_data = job_description,
            format_instructions = self.parser.get_format_instructions()
            )
        
        # Call LLM 
        response = safe_llm_call(lambda: self.llm.invoke(prompt))

        # Parse and validate structured output
        result = self.parser.parse(response.content)

        return result
    

