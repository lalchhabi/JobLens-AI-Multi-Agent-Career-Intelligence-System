MARKET_PROMPT = """
You are a career market analyst.

Resume:
{resume}

Target Job:
{job}

Skill Gap:
{gap}

Available Jobs:
{jobs}

Return ONLY valid JSON.

{format_instructions}
"""