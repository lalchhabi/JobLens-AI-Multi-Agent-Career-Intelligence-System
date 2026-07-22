# Define details prompt for job description
JOB_PROMPT = """
You are an expert job description analyzer.

Extract structured information from the job description.

Expected output format:

{output_format}

Job Description:
{job_description}

Rules:
- Extract the job title.
- Extract the hiring company.
- Extract required skills.
- Extract preferred skills separately.
- Extract experience level if mentioned.
- Extract responsibilities.
- Do not hallucinate information.
- If information is missing, use null or an empty list.
- Return ONLY valid JSON.
- Do not include explanations or markdown.
"""


JOB_OUTPUT_FORMAT = """
Return ONLY valid JSON in the following format.

{
    "title": "",
    "company": "",
    "required_skills": [],
    "preferred_skills": [],
    "experience_level": "",
    "responsibilities": []
}
"""