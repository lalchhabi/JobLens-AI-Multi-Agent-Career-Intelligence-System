# Import Required Libraries
from langchain_core.tools import tool

# Import project files
from services.adzuna_job_service import AdzunaService
from schemas.job_listing_schema import JobListingSchema

service = AdzunaService()
@tool
def search_jobs(
    query: str,
    country: str,
    results_per_page: int = 5
):
    """
    Search live job listings.

    This method delegates the search request to the underlying
    job provider service and returns standardized job listings.

    Args:
        query:
            Job title or keywords.

        country:
            Two-letter country code.

        results_per_page:
            Maximum number of jobs to retrieve.

    Returns:
        A list of standardized job listings.

    """

    jobs = service.search_jobs(
        query=query,
        country=country,
        results_per_page=results_per_page
    )

    
    # Return job listings with a shortened description
    return [
        {
            **job.model_dump(),

            # Limit the job description to the first 300 characters to reduce LLM token usage while still providing enough context about the role.
            "description": (
                job.description[:300] + "..."
                if len(job.description) > 300
                else job.description
            ),
        }
        for job in jobs
    ]