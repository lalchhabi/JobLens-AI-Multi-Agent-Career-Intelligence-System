# Detailed prompt to extract information from the resume

RESUME_PROMPT = """
You are an expert resume parser.

Extract structured information from the given resume text below.

{format_instructions}

Resume Text:
{resume_text}

Rules:
- Do not include explanation, markdown, or text
- Do not hallucinate information
- If something is missing, use empty list or null
- Keep skills precise
"""

