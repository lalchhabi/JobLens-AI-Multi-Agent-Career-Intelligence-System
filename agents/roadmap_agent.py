# Import libraries
from langchain_core.output_parsers import PydanticOutputParser
import json

# Import project files
from schemas.roadmap_schema import RoadmapSchema
from schemas.gap_schema import GapSchema
from schemas.job_schema import JobSchema
from prompts.roadmap_prompt import ROADMAP_PROMPT
from services.llm_service import get_llm_model
from utils.llm_retry import safe_llm_call


class RoadmapAgent():
    """Generates a personalized learning roadmap based on:

    - Gap Analysis
    - Target Job requirements

    The roadmap provides structured learning tasks,
    hands-on projects, and interview preparation guidance.
    """
    def __init__(self):
        # Initialize LLM model
        self.llm = get_llm_model()
        self.agent_name = "Roadmap Agent"
        # Create pydantic parser for structured output validation
        self.parser = PydanticOutputParser(pydantic_object=RoadmapSchema)


    def generate_roadmap(
            self, 
            gap_data: GapSchema,
            job_data: JobSchema,
            ) -> RoadmapSchema:
        """
        Generate a personalized learning roadmap based on
        skill gap analysis and target job requirements.

        Args:
            gap_data (GapSchema):
                Gap analysis result containing missing skills,
                strong skills, match score, and learning recommendations.

            job_data (JobSchema):
                Target job information including required skills,
                preferred skills, responsibilities, and experience level.

        Returns:
            RoadmapSchema:
                Structured learning roadmap with daily goals,
                projects, and interview preparation tasks.
        """

        # Finalize the prompt
        prompt = ROADMAP_PROMPT.format(
            gap_analysis = json.dumps(gap_data, indent=2, default=str),
            job_requirements = json.dumps(job_data, indent=2, default=str),
            format_instructions = self.parser.get_format_instructions()
        )

        print(f"Roadmap Agent prompt length: {len(prompt)}")

        # Call the model and generate the response
        response = safe_llm_call(
        lambda: self.llm.invoke(prompt),
        prompt=prompt,
        agent_name=self.agent_name,
    )

        # Convert the raw result into structured output
        result = self.parser.parse(response.content)

        return result