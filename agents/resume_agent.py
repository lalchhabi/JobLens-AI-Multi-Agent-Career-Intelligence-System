# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from services.llm_service import get_llm_model
from prompts.resume_prompt import RESUME_PROMPT
from schemas.resume_schema import ResumeSchema
from utils.llm_retry import safe_llm_call

class ResumeAgent:
    """ResumeAgent is responsible for converting raw resume text into a structured ResumeSchema using an LLM.
    """
    def __init__(self):
        # Initialize llm model
        self.llm = get_llm_model()

        # Create pydantic parser for structured output validation
        self.parser = PydanticOutputParser(pydantic_object=ResumeSchema)
    
    def parse_resume(self, resume_text:str) -> ResumeSchema:
        "Parse raw resume text into a structured ResumeSchema object."

        # Build final prompt with resume text and schema rules
        prompt = RESUME_PROMPT.format(
            format_instructions = self.parser.get_format_instructions(),
            resume_text = resume_text

        )

        # Call LLM
        response = safe_llm_call(lambda: self.llm.invoke(prompt))

        # Parse LLM output into structured Pydantic object
        result = self.parser.parse(response.content)
        return result






