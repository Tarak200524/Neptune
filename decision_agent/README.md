# Personal Decision Debate AI Agent

A Telegram-based AI decision partner that helps you make better decisions by analyzing, challenging, and debating your ideas.

## Features
- **Decision Analyzer**: Understands the category, seriousness, and emotional influence of your decision.
- **Supporter Agent**: Argues for your idea, finding benefits and opportunities.
- **Critic Agent (Devil's Advocate)**: Challenges your assumptions and identifies hidden risks.
- **Judge Agent**: Provides a balanced final recommendation with a confidence score and next action.

## Tech Stack
- **Backend**: Python, FastAPI
- **Agent Framework**: LangGraph, LangChain
- **LLM**: DeepSeek API (OpenAI-compatible)
- **Messaging**: Telegram Bot API

## Setup

1. **Clone the repository** (if applicable) and navigate to the project folder.

2. **Create a `.env` file**:
   Copy `.env.example` to `.env` and fill in your credentials.
   ```bash
   cp .env.example .env
   ```

3. **Install dependencies**:
   It's recommended to use the provided virtual environment.
   ```bash
   # If you haven't created it yet
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Unix/macOS:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Expose your local server**:
   Use ngrok to expose your port 8000 to the internet.
   ```bash
   ngrok http 8000
   ```

6. **Set the Telegram Webhook**:
   Send a POST request to Telegram to set your webhook URL.
   ```bash
   # Replace <YOUR_TOKEN> and <YOUR_NGROK_URL>
   curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=<YOUR_NGROK_URL>/telegram/webhook"
   ```

## Usage
Message your Telegram bot with any decision you're facing, for example:
- "Should I buy a new iPhone?"
- "Should I switch from React to Vue for my next project?"
- "Should I accept the new job offer in Berlin?"

The bot will analyze your request and provide a detailed debate and final recommendation.
