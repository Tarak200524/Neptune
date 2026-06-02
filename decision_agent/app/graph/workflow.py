from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from app.agents.analyzer_agent import analyzer_node
from app.agents.supporter_agent import supporter_node
from app.agents.critic_agent import critic_node
from app.agents.judge_agent import judge_node

class AgentState(TypedDict):
    user_message: str
    analysis: str
    support_points: str
    critical_points: str
    final_answer: str

def create_workflow():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("analyzer", analyzer_node)
    workflow.add_node("supporter", supporter_node)
    workflow.add_node("critic", critic_node)
    workflow.add_node("judge", judge_node)
    
    # Define edges
    workflow.add_edge(START, "analyzer")
    workflow.add_edge("analyzer", "supporter")
    workflow.add_edge("supporter", "critic")
    workflow.add_edge("critic", "judge")
    workflow.add_edge("judge", END)
    
    return workflow.compile()

app_workflow = create_workflow()
