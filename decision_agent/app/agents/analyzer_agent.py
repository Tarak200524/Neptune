import os
from app.services.deepseek_service import get_deepseek_client
from langchain_core.messages import SystemMessage, HumanMessage

def get_prompt(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
    with open(path, "r") as f:
        return f.read()

async def analyzer_node(state):
    llm = get_deepseek_client()
    system_prompt = get_prompt("analyzer.txt")
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=state["user_message"])
    ]
    
    response = await llm.ainvoke(messages)
    return {"analysis": response.content}
