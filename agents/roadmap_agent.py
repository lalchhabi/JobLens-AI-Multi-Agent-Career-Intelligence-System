# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from schemas.roadmap_schema import RoadmapSchema
from schemas.gap_schema import GapSchema
from schemas.job_schema import JobSchema
from prompts.roadmap_prompt import ROADMAP_PROMPT
from services.llm_service import get_llm_model


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
            gap_analysis = gap_data.model_dump_json(indent=2),
            job_requirements = job_data.model_dump_json(indent=2),
            format_instructions = self.parser.get_format_instructions()
        )

        # Call the model and generate the response
        response = self.llm.invoke(prompt)

        # Convert the raw result into structured output
        result = self.parser.parse(response.content)

        return result