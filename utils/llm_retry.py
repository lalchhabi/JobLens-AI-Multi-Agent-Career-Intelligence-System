# Import libraries
import time
from groq import RateLimitError

# Import project files
from utils.logger import get_logger

# Initialize logger 
logger = get_logger(__name__)


def safe_llm_call(fn, retries: int = 3, base_delay: int = 2):
    """Retry wrapper for LLM calls with exponential backoff.

    Args:
        fn (function): function that calls LLM
        retries (int, optional): Number of retries attempt. Defaults to 3.
        base_delay (int, optional): Starting wait time in seconds. Defaults to 2.
    """

    for attempt in range(retries):
        try:
            return fn()
        
        except RateLimitError as e:
            wait_time = base_delay * (2** attempt)

            logger.warning(
                f"Rate Limit hit. Retry {attempt + 1} / {retries}"
                f"waiting {wait_time}s...."
            )

            time.sleep(wait_time)

    raise Exception("LLM rate limit exceeded after retries")
