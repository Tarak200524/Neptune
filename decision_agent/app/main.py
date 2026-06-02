import logging
from fastapi import FastAPI, Request
from app.graph.workflow import app_workflow
from app.services.telegram_service import send_telegram_message

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Decision AI Agent")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    logger.info(f"Received telegram update: {data}")
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_text = data["message"].get("text", "")
        
        if user_text:
            if user_text == "/start":
                await send_telegram_message(chat_id, "Welcome to the Decision Debate AI. Send me any decision or question you're facing, and I'll analyze it for you!")
                return {"status": "ok"}
            
            # Inform user that analysis is starting
            await send_telegram_message(chat_id, "🔍 Analyzing your decision... Please wait.")
            
            try:
                # Run LangGraph workflow
                initial_state = {
                    "user_message": user_text,
                    "analysis": "",
                    "support_points": "",
                    "critical_points": "",
                    "final_answer": ""
                }
                
                result = await app_workflow.ainvoke(initial_state)
                final_response = result["final_answer"]
                
                # Send result back to Telegram
                await send_telegram_message(chat_id, final_response)
                
            except Exception as e:
                import traceback
                
                print("========== REAL ERROR ==========")
                print(str(e))
                traceback.print_exc()
                print("================================")
                
                await send_telegram_message(chat_id, f"Debug Error: {str(e)}")
    
    return {"status": "ok"}
