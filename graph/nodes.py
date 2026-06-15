# Import project files 
from services.career_analysis_service import CareerAnalysisService

service = CareerAnalysisService()


# Functions for the graph nodes
def parser_node(state):
    raw_resume = service.parser.extract_text(
        state["resume_path"]
    )

    return {
        "raw_resume": raw_resume,
        "raw_job": state["job_description"]
    }


def resume_node(state):
    result = service.resume_agent.parse_resume(
        state["raw_resume"]
    )

    return {
        "resume_analysis": result
    }

def job_node(state):
    result = service.job_agent.analyze_job(
        state["raw_job"]
    )

    return {
        "job_analysis": result
    }


def gap_node(state):
    result = service.gap_agent.gap_analyze(
        state["resume_analysis"],
        state["job_analysis"]
    )

    return {
        "gap_analysis": result
    }

def interview_node(state):
    result = service.interview_agent.generate_interview_questions(
        project_info=state["resume_analysis"],
        job_description=state["job_analysis"],
        learning_recommend=state["gap_analysis"],
        difficult_level="medium"
    )

    return {
        "interview_analysis": result
    }


def roadmap_node(state):
    result = service.roadmap_agent.generate_roadmap(
        gap_data=state["gap_analysis"],
        job_data=state["job_analysis"]
    )

    return {
        "learning_roadmap": result
    }


