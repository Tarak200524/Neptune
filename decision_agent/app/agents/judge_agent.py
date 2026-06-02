import logging
import os
from app.services.gemini_service import llm
from langchain_core.messages import SystemMessage, HumanMessage

logger = logging.getLogger(__name__)

def get_prompt(filename):
    path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
    with open(path, "r") as f:
        return f.read()

async def judge_node(state):
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

    try:
        logger.info("Starting Judge Agent")
        response = await llm.ainvoke(messages)
        logger.info("Judge Agent Completed")
    except Exception as e:
        logger.exception(e)
        raise

    return {"final_answer": response.content}
