# Detailed prompt for Learning Roadmap Generation

ROADMAP_PROMPT = """
    You are a expert career mentor or counselor

    Based on:
    1. Gap Analysis:
    {gap_analysis}
   
    2. Target_job_requirements:
    {job_requirements}

    Create a practical 14-day learning roadmap

    Focus on:
    - Daily learning goals
    - Hands on practice
    - Small projects
    - Interview preparation

    Output should be in this format:
    {format_instructions}

    Rules:
    - Return only valid JSON file
    - Do not add explanation
    - Do not use markdown
    - Keep tasks realistic and actionable
    
    """