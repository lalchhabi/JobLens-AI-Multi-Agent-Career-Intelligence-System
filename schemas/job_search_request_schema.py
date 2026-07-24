from pydantic import BaseModel, Field


class JobSearchRequestSchema(BaseModel):
    """
    Request schema for searching live job vacancies.

    This schema represents the user input required to query the
    Adzuna Job Search API. It is sent from the frontend whenever
    a user searches for live jobs from the Market section.

    Attributes:
        role:
            The target job title or search keywords entered by the user.
            This value is mapped to Adzuna's `what` query parameter.

        country:
            The two-letter ISO country code indicating the job market
            to search. Examples include:
                - "au" : Australia
                - "ca" : Canada
                - "gb" : United Kingdom
                - "us" : United States
                - "sg" : Singapore
                - "in" : India
                - "nz" : New Zealand
    """

    role: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description=(
            "Target job title or search keywords used to retrieve "
            "matching live job vacancies."
        ),
        examples=["AI Engineer"],
    )

    country: str = Field(
        default="au",
        min_length=2,
        max_length=2,
        description=(
            "Two-letter ISO country code specifying which country's "
            "job market should be searched."
        ),
        examples=["au"],
    )