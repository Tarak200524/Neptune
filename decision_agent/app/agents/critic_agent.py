import os
from app.services.gemini_service import llm
from langchain_core.messages import SystemMessage, HumanMessage

def get_prompt(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
    with open(path, "r") as f:
        return f.read()

async def critic_node(state):
    system_prompt = get_prompt("critic.txt")
    
    content = f"User Decision: {state['user_message']}\n\nAnalysis context: {state['analysis']}\n\nSupport arguments: {state['support_points']}"
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=content)
    ]
    
    response = await llm.ainvoke(messages)
    return {"critical_points": response.content}
