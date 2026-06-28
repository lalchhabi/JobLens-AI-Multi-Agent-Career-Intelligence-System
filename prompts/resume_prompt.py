# Detailed prompt to extract information from the resume

RESUME_PROMPT = """
You are an expert resume parser.

Extract structured information from the given resume text below.

Expected output format:
{output_format}

Resume Text:
{resume_text}

Rules:
- Do not include explanation, markdown, or text
- Do not hallucinate information
- If something is missing, use empty list or null
- Keep skills precise
"""

RESUME_OUTPUT_FORMAT = """
Return ONLY valid JSON in the following format.

{
    "name": "",
    "email": "",
    "skills": [],
    "projects": [
        {
            "name": "",
            "description": "",
            "tech_stack": []
        }
    ],
    "experience": [
        {
            "company": "",
            "role": "",
            "duration": "",
            "responsibilities": []
        }
    ],
    "education": [
        {
            "institution": "",
            "degree": "",
            "year": ""
        }
    ]
}
"""