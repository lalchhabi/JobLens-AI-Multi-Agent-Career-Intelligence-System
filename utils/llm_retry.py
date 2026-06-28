# Import libraries
import time
from groq import RateLimitError

# Import project files
from utils.logger import get_logger

# Initialize logger 
logger = get_logger(__name__)

def estimate_tokens(text: str) -> int:
    """
    Rough token estimation.
    Assumption:
        1 token ≈ 4 characters
    """
    return len(text) // 4


def safe_llm_call(fn, 
                  prompt: str,
                  agent_name: str,
                  retries: int = 3, 
                  base_delay: int = 2
                  ):
    """Retry wrapper for LLM calls with exponential backoff.

    Args:
        fn (function): function that calls LLM
        prompt(str): Prompt that used for generating response
        agent_name(str): Name of the Agent
        retries (int, optional): Number of retries attempt. Defaults to 3.
        base_delay (int, optional): Starting wait time in seconds. Defaults to 2.
    """
    prompt_chars = len(prompt)
    prompt_tokens = estimate_tokens(prompt)

    logger.info("=" * 60)
    logger.info(f"Agent              : {agent_name}")
    logger.info(f"Prompt Characters  : {prompt_chars}")
    logger.info(f"Estimated Tokens   : {prompt_tokens}")
    
    for attempt in range(retries):
        logger.info("Entering safe_llm_call")
        try:
            start = time.time()

            response = fn()

            latency = time.time() - start
            response_tokens = estimate_tokens(response.content)
            
            logger.info(f"Response Tokens : {response_tokens}")
            logger.info(f"Total Tokens    : {prompt_tokens + response_tokens}")
            logger.info(f"Latency        : {latency:.2f} sec")
            logger.info("=" * 60)

            return response
        
        except RateLimitError as e:
            wait_time = base_delay * (2** attempt)

            logger.warning(
                f"Rate Limit hit. Retry {attempt + 1} / {retries}"
                f"waiting {wait_time}s...."
            )

            time.sleep(wait_time)

        except Exception as e:
            logger.error(f"Caught exception: {type(e)}")
            logger.error(e)
            raise
    raise Exception("LLM rate limit exceeded after retries.")