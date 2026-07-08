# Import libraries
from langchain_core.output_parsers import PydanticOutputParser

# Import project files
from prompts.gap_prompt import GAP_PROMPT, FORMAT_INSTRUCTIONS
from schemas.gap_schema import GapSchema, GapLLMSchema
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from services.llm_service import get_llm_model
from services.skill_normalize import normalize_skills
from utils.llm_retry import safe_llm_call
from utils.logger import get_logger
import services.scoring_engine as scoring_engine
from services.context_builder import build_gap_context

# Define logger
logger = get_logger(__name__)


# Gap Analysis Agent
class GapAnalysisAgent:
    """
    GapAnalysisAgent compares a candidate's resume with a job description
    and generates a structured gap analysis report using an LLM.

    Responsibilities:
    - Perform semantic skill matching using the LLM
    - Extract matched and missing skills
    - Generate learning recommendations
    - Compute deterministic match score using the scoring engine
    """

    def __init__(self):

        # Initialize LLM model
        self.llm = get_llm_model()
        self.agent_name = "Gap Agent"

        # Pydantic parser ensures structured output (GapSchema validation)
        self.parser = PydanticOutputParser(
            pydantic_object=GapLLMSchema
        )

    def gap_analyze(self, resume_detail:str, job_description:str)-> GapSchema:
        """
        Perform gap analysis between resume and job description.

        Args:
            resume_data (str): Structured or raw resume text/data
            job_data (str): Job description text

        Returns:
            GapSchema: Structured gap analysis result
        """
        

        # Parse resume into schema
        resume = ResumeSchema(**resume_detail)
        job = JobSchema(**job_description)

        # Normalize job skills before sending them to the LLM
        job.required_skills = normalize_skills(job.required_skills)
        job.preferred_skills = normalize_skills(job.preferred_skills)

        resume_context = build_gap_context(resume)

        prompt = GAP_PROMPT.format(
            resume_data = resume_context, 
            job_data = job.model_dump(),
            format_instructions = FORMAT_INSTRUCTIONS
            )
        
        # Call LLM 
        response = safe_llm_call(
            lambda: self.llm.invoke(prompt),
            prompt=prompt,
            agent_name=self.agent_name,
        )

        logger.info("===== RAW LLM RESPONSE =====")
        logger.info(response.content)


        # Parse only LLM Output
        llm_result: GapLLMSchema = self.parser.parse(response.content)

        # Validate the llm result for matched and missing skills
        matched = set(llm_result.matched_preferred_skills)
        missing = set(llm_result.missing_preferred_skills)

        duplicates = matched & missing

        if duplicates:
            logger.warning(
                f"Duplicate preferred skills detected: {duplicates}"
            )

        llm_result.missing_preferred_skills = list(
            set(llm_result.missing_preferred_skills)
            - set(llm_result.matched_preferred_skills)
        )

        try:

        # Calculate deterministic match score
            score = scoring_engine.calculate_match_score(
                matched_required_skills=llm_result.matched_required_skills,
                missing_required_skills=llm_result.missing_required_skills,
                matched_preferred_skills=llm_result.matched_preferred_skills,
                missing_preferred_skills=llm_result.missing_preferred_skills,
            )

        except Exception as e:
            logger.exception("Failed to calculate deterministic match score")
            raise

        # Parse and validate structured output
        result = GapSchema(
            matched_required_skills=llm_result.matched_required_skills,
            missing_required_skills=llm_result.missing_required_skills,
            matched_preferred_skills=llm_result.matched_preferred_skills,
            missing_preferred_skills=llm_result.missing_preferred_skills,
            learning_recommendation=llm_result.learning_recommendation,
            match_score=score,
        )

        logger.info("===== GAP PROMPT =====")
        logger.info(prompt)
        logger.info("======================")

        logger.info("LLM Gap Output:")
        logger.info(llm_result.model_dump())

        logger.info("Gap analysis started")
        logger.info(f"Final prompt size: {len(prompt)} characters")
        logger.info(
            f"Match Score: {result.match_score.overall_score}% "
            f"(Required: {result.match_score.required_skill_score}%, "
            f"Preferred: {result.match_score.preferred_skill_score}%)"
        )

        return result
            

