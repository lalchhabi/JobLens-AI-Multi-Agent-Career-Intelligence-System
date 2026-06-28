#import required libraries
from langchain_core.output_parsers import PydanticOutputParser
# import project files
from tools.job_search_tool import JobSearchTool
from schemas.market_schema import MarketSchema, JobRecommendation
from services.llm_service import get_llm_model
from utils.llm_retry import safe_llm_call
from prompts.market_prompt import MARKET_PROMPT
import json

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
        print(f"job objects: {job_objects}")

        # STEP 3: Build prompt
        prompt = MARKET_PROMPT.format(
            resume=json.dumps(resume_analysis, indent=2, default=str),
            job=json.dumps(job_analysis, indent=2, default=str),
            gap=json.dumps(gap_analysis, indent = 2, default = str),
            jobs=json.dumps(jobs, indent=2),
            format_instructions = self.parser.get_format_instructions()
        )

        # STEP 4: LLM call
        # Call the LLM model
        response = safe_llm_call(
            lambda: self.llm.invoke(prompt),
            prompt=prompt,
            agent_name=self.agent_name,
        )

        result = self.parser.parse(response.content)

        # STEP 5: Inject real jobs 
        # result.recommended_jobs = job_objects

        return result

        