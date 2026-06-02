import os
from app.services.gemini_service import llm
from langchain_core.messages import SystemMessage, HumanMessage

def get_prompt(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
    with open(path, "r") as f:
        return f.read()

async def analyzer_node(state):
    system_prompt = get_prompt("analyzer.txt")
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=state["user_message"])
    ]
    
    response = await llm.ainvoke(messages)
    return {"analysis": response.content}
