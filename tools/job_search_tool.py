# Import required libraries
from duckduckgo_search import DDGS
import json

class JobSearchTool():
    def __init__(
        self,
        file_path: str = "mock_jobs.json"
            ):
        self.file_path = file_path
        
    def search_jobs(
        self,
        target_role: str,
        limit: int = 5
    ):
        with open(self.file_path, "r") as f:
            jobs = json.load(f)

        target_role = target_role.lower()

        # simple filtering logic
        filtered = [
            job for job in jobs
            if target_role in job['title'].lower()
            or target_role in job['company'].lower()
        ]

        # fallback if nothing marches
        if not filtered:
            filtered = jobs

        return filtered[:limit]


    def search_similar_roles(
            self, 
            target_role: str,
            max_results: int = 10
            ):
        
        results = []

        query = f"{target_role} jobs"

        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                max_results=max_results
            )
        
        for item in search_results:
            results.append({
                "title": item.get('title'),
                "body": item.get("body"),
                "url": item.get("href")

            })
    
        return results