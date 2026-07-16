# Import Required Libraries
from typing import Optional
from pydantic import BaseModel, Field

class JobListingSchema(BaseModel):

    title: str = Field(
        description = "Job title advertised by the employer.")

    company: str = Field(
        description = "Company or organization hiring for the position."
    )

    location: str = Field(
        description = "Job Location including city, state or country."
    )

    description: str = Field(
        description = "Full job description provided in the job advertisement."

    )

    apply_url: str = Field(
        description="Direct URL where the candidate can view or apply for the job."
    )

    salary_min: Optional[int] = Field(
        default=None,
        description="Minimum annual salary offered for the position, if available."
    )

    salary_max: Optional[int] = Field(
        default=None,
        description="Maximum annual salary offered for the position, if available."
    )

    contract_type: Optional[str] = Field(
        default=None,
        description="Employment type such as Full-time, Part-time, or Contract."
    )

    created: Optional[str] = Field(
        default=None,
        description="Date when the job was posted."
    )
