# Import libraries
from langgraph.graph import StateGraph, START, END

# Import project files
from graph.state import CareerState
from graph.nodes import (
    parser_node,
    resume_node,
    job_node,
    gap_node,
    interview_node,
    roadmap_node,
    market_node
)

# Define StateGraph nodes and edges
builder = StateGraph(CareerState)
builder.add_node("parser", parser_node)
builder.add_node("resume", resume_node)
builder.add_node("job", job_node)
builder.add_node("gap", gap_node)
builder.add_node("interview", interview_node)
builder.add_node("roadmap", roadmap_node)
builder.add_node("market", market_node)

builder.add_edge(START, "parser")
builder.add_edge("parser", "resume")
builder.add_edge("resume", "job")
builder.add_edge("job", "gap")
builder.add_edge("gap", "interview")
builder.add_edge("gap", "interview")
builder.add_edge("gap", "market")

builder.add_edge("interview", END)
builder.add_edge("roadmap", END)
builder.add_edge("market", END)

career_graph = builder.compile()



