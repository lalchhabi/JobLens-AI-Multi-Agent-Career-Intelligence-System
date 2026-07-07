#import required libraries
from langchain_core.output_parsers import PydanticOutputParser
# import project files
from tools.job_search_tool import JobSearchTool
from schemas.market_schema import MarketSchema, JobRecommendation
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema
from services.llm_service import get_llm_model
from utils.llm_retry import safe_llm_call
from prompts.market_prompt import MARKET_PROMPT
import json
from services.context_builder import build_market_context
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class MarketAgent:

    def __init__(self):
        self.job_tool = JobSearchTool()
        self.llm = get_llm_model()
        self.agent_name = "Market Agent"
        self.parser = PydanticOutputParser(pydantic_object=MarketSchema)

    def analyze_market(
        self,
        resume_analysis,
        job_analysis,
        gap_analysis
    ):
        """Generate labor market insights for the candidate.

        Workflow:
        1. Reconstruct schema objects from serialized graph state.
        2. Build a compact market context to reduce prompt size.
        3. Retrieve similar jobs from the job search tool.
        4. Generate market insights using the LLM.
        5. Return structured market analysis.

        Using an optimized context significantly reduces token usage
        without sacrificing recommendation quality.

        """
        # Step 1: Get Jobs from tool
        jobs = self.job_tool.search_similar_roles(
            target_role=job_analysis['title'],
            max_results=5
        )


        # STEP 2: Convert to schema objects
        job_objects = [
            JobRecommendation(**job)
            for job in jobs
        ]

        # Convert serialized graph state back into schema objects
        # so the context builder can access strongly typed attributes.

        resume = ResumeSchema(**resume_analysis)
        job = JobSchema(**job_analysis)
        gap = GapSchema(**gap_analysis)

        # Build a compact market context to reduce prompt size.
        market_context = build_market_context(
            resume,
            job,
            gap
        )

        # STEP 3: Build prompt
        prompt = MARKET_PROMPT.format(
        market_context=market_context,
        jobs=json.dumps(jobs, indent=2),
        format_instructions=self.parser.get_format_instructions()
    )

        # STEP 4: LLM call
        # Call the LLM model
        response = safe_llm_call(
            lambda: self.llm.invoke(prompt),
            prompt=prompt,
            agent_name=self.agent_name,
        )

        result = self.parser.parse(response.content)

        format_instructions = self.parser.get_format_instructions()

        logger.info("Market Agent Prompt Profile")
        logger.info(f"Final Prompt          : {len(prompt)}")

        return result

        