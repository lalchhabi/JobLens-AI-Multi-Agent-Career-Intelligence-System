# Detailed prompt instruction for gap analysis

GAP_PROMPT = """
    You are an expert technical recruiter.
    Compare the candidate's resume against the job description and identify skill gaps.

    CANDIDATE RESUME: 
    {resume_data}

    JOB_DESCRIPTION:
    {job_data}

    You MUST follow this exact structure:
    {format_instructions}

    RULES:
    1. Skill Matching Rules:
    - Match skills semantically, including common abbreviations and equivalent terms.
    - Identify both direct and related skill matches

    2. Strong Skills:
    - Skills present in resume that align with the job requirements.

    3. Missing Skills:
    - Skills required in job but not present or weak in resume.

    4. Learning Recommendations:
    - Provide concise learning recommendations including relevant courses, projects, or tools.
    - Make recommendation realistic for a job seeker.
    
    5. IMPORTANT:
    - Do not hallucinate skills.
    - Return ONLY valid JSON matching the schema.
    - Do not include explanations, markdown, code blocks, or any extra text.

    FINAL RULE:
    - Your response MUST be valid JSON.
    - JSON does NOT support comments.
    - Do NOT use // comments.
    - Do NOT use /* */ comments.
    - Do NOT explain any field.
    - Do NOT add notes.
    - Do NOT duplicate skills.
    - A skill CANNOT appear in both matched and missing lists.
    """