import os
from app.services.deepseek_service import get_deepseek_client
from langchain_core.messages import SystemMessage, HumanMessage

def get_prompt(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
    with open(path, "r") as f:
        return f.read()

async def judge_node(state):
    llm = get_deepseek_client()
    system_prompt = get_prompt("judge.txt")
    
    content = (
        f"User Decision: {state['user_message']}\n\n"
        f"Analysis: {state['analysis']}\n\n"
        f"Supportive Arguments: {state['support_points']}\n\n"
        f"Critical Arguments: {state['critical_points']}"
    )
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=content)
    ]
    
    response = await llm.ainvoke(messages)
    return {"final_answer": response.content}
