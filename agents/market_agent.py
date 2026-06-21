# import project files
from tools.job_search_tool import JobSearchTool
class MarketAgent:

    def __init__(self):
        self.job_tool = JobSearchTool()

    def analyze_market(
        self,
        resume_analysis,
        job_analysis
    ):

        jobs = self.job_tool.search_similar_roles(
            job_analysis.title
        )

        