# Import Required Libraries
from dotenv import load_dotenv
import os
import requests
from schemas.job_listing_schema import JobListingSchema


# Load Environment variables
load_dotenv()


# Create the service class
class AdzunaService:
    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    def __init__(self):
        self.app_id = os.getenv("ADZUNA_APP_ID")
        self.app_key = os.getenv("ADZUNA_API_KEY")


    # Create the public method
    def search_jobs(
            self,
            query:str,
            country:str,
            results_per_page: int = 5
    )-> list[JobListingSchema]:
        """
        Search for job listings from the Adzuna API.

    Args:
        query: Job title or keywords to search for.
        country: Two-letter country code (e.g., "au", "ca", "gb").
        results_per_page: Maximum number of job listings to retrieve.

    Returns:
        A list of JobListingSchema objects matching the search query.
        """

        # Build the request
        url = (
            f"{self.BASE_URL}/"
            f"{country.lower()}/search/1"
        )

        # Build the parameters
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": results_per_page,
            "what": query
        }

        # Send the request
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )

        # Check for wrrors
        if response.status_code != 200:
            response.raise_for_status()

        # Parse the JSON
        data = response.json()

        # Convert results

        jobs = []

        for job in data.get('results',[]):
            jobs.append(
                self._convert_job(job)
            )

        return jobs
    

    def _convert_job(self, job_data: dict) -> JobListingSchema:
        """
        Convert a raw Adzuna job listing into a JobListing object.

        This helper method extracts the relevant fields from the JSON
        response returned by the Adzuna API and maps them to the
        application's standardized JobListing schema.

        Args:
            job: A dictionary representing a single job listing returned
                by the Adzuna API.

        Returns:
            A JobListingSchema object containing the normalized job information.
        """

        company = job_data.get("company", {})
        location = job_data.get("location", {})

        return JobListingSchema(

            title=job_data.get("title"),

            company=company.get("display_name"),

            location=location.get("display_name"),

            description=job_data.get("description"),

            apply_url=job_data.get("redirect_url"),

            created=job_data.get("created"),

            salary_min=job_data.get("salary_min"),

            salary_max=job_data.get("salary_max"),


        )