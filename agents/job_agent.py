# Import libraries 
from langchain_core.output_parsers import PydanticOutputParser

# Import project files 
from prompts.job_prompt import JOB_PROMPT
from services.llm_service import get_llm_model
from schemas.job_schema import JobSchema


class JOBAGENT:
    def __init__(self):
        # Initialize llm model
        self.llm_model = get_llm_model()

         # Create pydantic parser for structured output validation
        self.parser = PydanticOutputParser(pydantic_object=JobSchema)

    def analyze_job(self, job_description:str)-> JobSchema:
        """Analyze job description and store them in structured format

        Args:
            job_description (str): Raw Job description

        Returns:
            JobSchema: Structured output results based on job schema
        """
        
        # Finalize prompt
        prompt = JOB_PROMPT.format(
            format_instructions = self.parser.get_format_instructions(),
            job_description = job_description
        )

        # Call the LLM model
        response = self.llm_model.invoke(prompt)

        # Parse LLM output into structured Pydantic object
        result = self.parser.parse(response.content)

        return result
    
    
