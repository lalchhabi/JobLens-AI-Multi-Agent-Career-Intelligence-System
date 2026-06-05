# Define details prompt for job description
JOB_PROMPT = """
    You are an expert job description analyzer.

    Extract structured information from the job description.

    {format_instructions}

    Job Description:
    {job_description}

    Rules:
    - Extract required skills
    - Extract perferred skills separately.
    - Identify experience level if mentioned.
    - Extract key roles and responsibilities
    - Do not hallcinate information
    - Do not include explanation, markdown, or text
"""