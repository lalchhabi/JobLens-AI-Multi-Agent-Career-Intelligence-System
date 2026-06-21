# Import project files 
from tools.pdf_parser import PDFparser

from agents.resume_agent import ResumeAgent
from agents.job_agent import JobAgent
from agents.gap_agent import GapAnalysisAgent
from agents.interview_agent import InterviewAgent
from agents.roadmap_agent import RoadmapAgent
from agents.market_agent import MarketAgent

resume_agent = ResumeAgent()
job_agent = JobAgent()
gap_agent = GapAnalysisAgent()
interview_agent = InterviewAgent()
roadmap_agent = RoadmapAgent()
market_agent = MarketAgent()

parser = PDFparser()

# Functions for the graph nodes
def parser_node(state):
    raw_resume = parser.extract_text(state["resume_path"])
    
    return {
        "raw_resume": raw_resume,
        "raw_job": state['job_description']
    }

def resume_node(state):
    result = resume_agent.parse_resume(
        state["raw_resume"]
    )
    return {
        "resume_analysis": result.model_dump()
    }

def job_node(state):
    result = job_agent.analyze_job(
        state["job_description"]
    )
    return {
        'job_analysis': result.model_dump()
    }

def gap_node(state):
    result = gap_agent.gap_analyze(
        state["resume_analysis"],
        state["job_analysis"]
    )
    return {
        "gap_analysis":result.model_dump()
    }

def interview_node(state):
    result = interview_agent.generate_interview_questions(
        project_info=state["resume_analysis"],
        job_description=state["job_analysis"],
        learning_recommend=state["gap_analysis"],
        difficult_level="medium"
    )
    return {
        "interview_analysis":result.model_dump()
    }

def roadmap_node(state):
    result = roadmap_agent.generate_roadmap(
        gap_data=state["gap_analysis"],
        job_data=state["job_analysis"]
    )
    return {
        "learning_roadmap":result.model_dump()
    }

def market_node(state):
    result = market_agent.analyze_market(
        state['resume_analysis'],
        state['job_analysis']
    )

    return {
        "market_analysis":result.model_dump()
    }