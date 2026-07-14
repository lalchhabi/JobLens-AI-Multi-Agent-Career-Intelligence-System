# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from services.llm_service import get_llm_model
from prompts.resume_prompt import RESUME_PROMPT, RESUME_OUTPUT_FORMAT
from schemas.resume_schema import ResumeSchema
from utils.llm_retry import safe_llm_call
from utils.logger import get_logger

# Intialize logger 
logger = get_logger(__name__)

class ResumeAgent:
    """ResumeAgent is responsible for converting raw resume text into a structured ResumeSchema using an LLM.
    """
    def __init__(self):
        # Initialize llm model
        self.llm = get_llm_model()
        self.agent_name = "Resume Agent"

        # Create pydantic parser for structured output validation
        self.parser = PydanticOutputParser(pydantic_object=ResumeSchema)
    
    def parse_resume(self, resume_text:str) -> ResumeSchema:
        "Parse raw resume text into a structured ResumeSchema object."

        # Build final prompt with resume text and schema rules
        format_instructions = self.parser.get_format_instructions()
        prompt = RESUME_PROMPT.format(
            output_format = RESUME_OUTPUT_FORMAT,
            resume_text = resume_text
        )

        logger.info("Resume Agent Prompt Profile")
        logger.info(f"Prompt         : {len(RESUME_PROMPT)}")
        logger.info(f"Resume Text      : {len(resume_text)}")
        logger.info(f"Output Template  : {len(RESUME_OUTPUT_FORMAT)}")

        # Call LLM
        response = safe_llm_call(
        lambda: self.llm.invoke(prompt),
        prompt=prompt,
        agent_name=self.agent_name,
    )

        # Parse LLM output into structured Pydantic object
        result = self.parser.parse(response.content)

        logger.info(f"Resume Result: {result}")
        return result






