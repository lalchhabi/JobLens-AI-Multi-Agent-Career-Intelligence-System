# Import Required Libraries
from typing import Optional
from pydantic import BaseModel, Field

class JobListingSchema(BaseModel):
    """Standardized job listing returned by external job providers.
    This schema represents the normalized job information used throughout the Joblens application regardless of the underlying job provider (e.g. Adzuna, Linkedin, Jooble)
    """

    title: str = Field(
        description = "Job title advertised by the employer.")

    company: str = Field(
        description = "Company or organization hiring for the position."
    )

    location: str = Field(
        description = "Job Location including city, state or country."
    )

    job_description: str = Field(
        description = "Full job description provided in the job advertisement."

    )

    apply_url: str = Field(
        description="Direct URL where the candidate can view or apply for the job."
    )

    created: Optional[str] = Field(
        default=None,
        description="Date when the job was posted."
    )

    salary_min: Optional[int] = Field(
        default=None,
        description="Minimum annual salary offered for the position, if available."
    )

    salary_max: Optional[int] = Field(
        default=None,
        description="Maximum annual salary offered for the position, if available."
    )

