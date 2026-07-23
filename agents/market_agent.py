#import required libraries
from langchain_core.output_parsers import PydanticOutputParser

# import project files
from schemas.market_schema import MarketSchema
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
        self.analysis_llm = get_llm_model()
        self.agent_name = "Market Agent"
        self.parser = PydanticOutputParser(pydantic_object=MarketSchema)

    def analyze_market(
        self,
        resume_analysis,
        job_analysis,
        gap_analysis
    ):
        """
        Analyze the candidate's career market profile.

        This method generates market insights based on the candidate's
        resume, target job, and identified skill gaps.

        Workflow
        --------
        1. Convert graph state dictionaries into schema objects.
        2. Build a compact market context from the candidate profile.
        3. Generate market insights using the LLM.
        4. Parse the LLM response into a validated MarketSchema.
        5. Return the structured market analysis.
        """

        # Step 1: Convert graph state dictionaries into schema objects
        resume = ResumeSchema(**resume_analysis)
        target_job = JobSchema(**job_analysis)
        gap = GapSchema(**gap_analysis)

        # Step 2: Build the candidate market context
        market_context = build_market_context(
            resume,
            target_job,
            gap
        )

        # Step 3: Build the LLM prompt
        prompt = MARKET_PROMPT.format(
            market_context=market_context
        )

        logger.info(
            f"Market Agent Prompt Length: {len(prompt)} characters"
        )

        # Step 4: Generate market analysis
        response = safe_llm_call(
            lambda: self.analysis_llm.invoke(prompt),
            prompt=prompt,
            agent_name=self.agent_name,
        )

        logger.info("Market Agent Response:")
        logger.info(response.content)

        # Step 5: Parse and validate the response
        analysis = self.parser.parse(response.content)

        # Return the validated market analysis
        return analysis




        