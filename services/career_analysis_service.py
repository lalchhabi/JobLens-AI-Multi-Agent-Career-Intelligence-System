# Import project file

from schemas.career_analysis_schema import CareerAnalysisSchema
from utils.logger import get_logger
from graph.workflow import career_graph


# Initialize module-level logger
logger = get_logger(__name__)

class CareerAnalysisService():
    """
    Orchestrates the full AI career pipeline

    Resume -> Job -> Gap -> Interview -> Roadmap

    This is the core business logic layer of the system.
    """

    def career_analyze(self,
                       resume_path: str,
                       job_description: str
                    ) -> CareerAnalysisSchema:
        """Run full Career Intelligent Pipeline

        Args:
            resume_path (str): Path to resume pdf
            job_description (str): Job description 

        Returns:
            CareerAnalysisSchema: Complete AI analysis result
        """
        try:
            logger.info("Running LangGraph workflow")

            result = career_graph.invoke(
                {
                    "resume_path": resume_path,
                    "job_description": job_description,
                }
            )

            logger.info("Career analysis pipeline completed")

            return CareerAnalysisSchema(
                resume_analysis=result["resume_analysis"],
                job_analysis=result["job_analysis"],
                gap_analysis=result["gap_analysis"],
                interview_analysis=result["interview_analysis"],
                learning_roadmap=result["learning_roadmap"],
            )
        
        except Exception as e:
            logger.error(f"Career Analysis failed: {str(e)}")
            raise



    def career_analyze_stream(
        self, 
        resume_path: str, 
        job_description: str
        ):
        """Execute the JobLens AI workflow using LangGraph streaming.
        Instead of waiting for the entire workflow to complete,
        this method yields intermediate node outputs as they
        become available.

        Args:
            resume_path (str):
                Path to the uploaded resume file.

            job_description (str):
                Raw job description text provided by the user.
        """
        try:
            logger.info("Starting LangGraph streaming workflow")

            for event in career_graph.stream({
                "resume_path": resume_path,
                "job_description": job_description,
            }):

                # NORMALIZE EVENT FORMAT
                if not isinstance(event, dict):
                    continue

                # LangGraph usually returns: {node_name: state_update}
                for node_name, node_output in event.items():

                    if not isinstance(node_output, dict):
                        continue

                    # find actual meaningful key inside node output
                    for key, value in node_output.items():

                        # skip internal langgraph metadata
                        if key in ["event", "metadata"]:
                            continue

                        yield {
                            "type": key,
                            "data": 
                                value.model_dump()
                                if hasattr(value, "model_dump")
                                else value
                        }

            logger.info("Streaming workflow completed")

        except Exception as e:
            logger.exception(f"Streaming workflow failed")

            yield{
                "type":"error",
                "data":str(e)
            }
            
