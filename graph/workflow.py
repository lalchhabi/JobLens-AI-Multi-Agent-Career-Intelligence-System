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
    market_node,
    cover_letter_node
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
builder.add_node("cover_letter",cover_letter_node)

builder.add_edge(START, "parser")
builder.add_edge("parser", "resume")
builder.add_edge("resume", "job")
builder.add_edge("job", "gap")
builder.add_edge("gap", "interview")
builder.add_edge("gap", "market")
builder.add_edge("gap", "cover_letter")

builder.add_edge("interview", 'roadmap')
builder.add_edge("market", 'roadmap')
builder.add_edge("roadmap", END)
builder.add_edge("cover_letter", END)

career_graph = builder.compile()


# Visualize the graph
graph = career_graph.get_graph()
png_data = graph.draw_mermaid_png()

with open("career_graph.png", "wb") as f:
    f.write(png_data)

