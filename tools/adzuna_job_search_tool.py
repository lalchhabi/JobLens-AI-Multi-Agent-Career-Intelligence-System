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
    results_per_page: int = 10
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

    MAX_DESCRIPTION_LENGTH = 120

    
    # Return job listings with a shortened description
    MAX_DESCRIPTION_LENGTH = 150

    return [
        {
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "job_description": (
                job.job_description[:MAX_DESCRIPTION_LENGTH] + "..."
                if len(job.job_description) > MAX_DESCRIPTION_LENGTH
                else job.job_description
            ),
            "apply_url": job.apply_url
        }
        for job in jobs
    ]