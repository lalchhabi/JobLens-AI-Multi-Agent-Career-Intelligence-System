# Import project file
from schemas.resume_schema import ResumeSchema
from schemas.job_schema import JobSchema
from schemas.gap_schema import GapSchema

def build_gap_context(resume: ResumeSchema) -> str:
    """
    Build a compact resume context for the Gap Analysis Agent.
    Includes only the information needed for skill matching.
    """

    sections = []

    sections.append("Skills:\n" + "\n".join(resume.skills))

    if resume.projects:
        projects = "\n".join(
            f"- {p.name}: {', '.join(p.tech_stack)}"
            for p in resume.projects
        )
        sections.append("Projects:\n" + projects)

    if resume.experience:
        experience = "\n".join(
            f"- {e.role} @ {e.company}"
            for e in resume.experience
        )
        sections.append("Experience:\n" + experience)

    return "\n\n".join(sections)


def build_interview_context(
    resume: ResumeSchema,
    job: JobSchema,
    gap: GapSchema,
) -> str:
    """
    Build a compact context for the Interview Agent.

    Includes only the information required to generate
    personalized interview questions.
    """

    experiences = "\n".join(
        f"- {exp.role} at {exp.company}"
        for exp in resume.experience
    )

    projects = "\n".join(
        f"- {project.name}"
        for project in resume.projects
    )

    context = f"""
    Candidate Skills:
    {", ".join(resume.skills)}

    Experience:
    {experiences}

    Projects:
    {projects}

    Target Role:
    {job.title}

    Required Skills:
    {", ".join(job.required_skills)}

    Matched Skills:
    {", ".join(gap.matched_required_skills)}

    Missing Skills:
    {", ".join(gap.missing_required_skills)}
    """

    return context.strip()
    

def build_market_context(
        resume: ResumeSchema,
        job: JobSchema,
        gap: GapSchema
) -> str:
    """
    Build a compact context for the Market Agent.
    """

    context = f"""
    Candidate Skills:
    {", ".join(resume.skills)}

    Experience:
    {", ".join(f"{exp.role} at {exp.company}" for exp in resume.experience)}

    Target Role:
    {job.title}

    Matched Required Skills:
    {", ".join(gap.matched_required_skills)}

    Missing Required Skills:
    {", ".join(gap.missing_required_skills)}

    Learning Recommendations:
    {", ".join(gap.learning_recommendation)}
    """

    return context.strip()