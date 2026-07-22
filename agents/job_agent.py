# Import libraries 
from langchain_core.output_parsers import PydanticOutputParser

# Import project files 
from prompts.job_prompt import JOB_PROMPT, JOB_OUTPUT_FORMAT
from services.llm_service import get_llm_model
from schemas.job_schema import JobSchema
from utils.llm_retry import safe_llm_call


class JobAgent:
    """JobAgent is responsible for converting raw job description text into structure JobSchema using an LLM
    """
    def __init__(self):
        # Initialize llm model
        self.llm_model = get_llm_model()
        self.agent_name = "Job Agent"
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
            output_format = JOB_OUTPUT_FORMAT,
            job_description = job_description
        )


        # Call the LLM model
        response = safe_llm_call(
            lambda: self.llm_model.invoke(prompt),
            prompt=prompt,
            agent_name=self.agent_name,
        )

        # Parse LLM output into structured Pydantic object
        result = self.parser.parse(response.content)

        return result
    
    
