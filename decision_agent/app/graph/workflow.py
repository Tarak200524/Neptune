from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from app.agents.decision_agent import decision_node

class AgentState(TypedDict):
    user_message: str
    final_answer: str

def create_workflow():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("decision_agent", decision_node)
    
    # Define edges
    workflow.add_edge(START, "decision_agent")
    workflow.add_edge("decision_agent", END)
    
    return workflow.compile()

app_workflow = create_workflow()
