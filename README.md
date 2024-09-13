# 🤖 Gemini AI Telegram Chatbot

This project is a **Telegram Chatbot** powered by **Google Gemini AI**, allowing users to interact with the latest AI model directly through Telegram. The bot is capable of answering questions, engaging in conversations, and providing intelligent responses on various topics.

## ✨ Features
- **Conversational AI** using the Google Gemini API.
- **Real-time interaction** through Telegram.
- **Contextual and natural** conversation flow.
- **Easy deployment** with Docker support.

## 🚀 Getting Started

Follow these steps to set up and run the bot locally.

### 1. Clone the repository
```bash
git clone https://github.com/XredaX/chatbot-telegram
cd chatbot-telegram
```

### 2. Install dependencies
Make sure you have Python installed. Then, run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
You need to set two environment variables for the bot to function properly:

- `API_KEY`: Your Google Gemini API key
- `BOT_TOKEN`: Your Telegram bot token

You can set these in your environment or use a `.env` file:
```bash
export API_KEY="your_gemini_api_key"
export BOT_TOKEN="your_telegram_bot_token"
```

Alternatively, create a `.env` file in the root directory of the project:
```
API_KEY=your_gemini_api_key
BOT_TOKEN=your_telegram_bot_token
```

### 4. Configure the Gemini API and Telegram Bot

The bot will fetch these environment variables during runtime:
```python
genai.configure(api_key=os.getenv('API_KEY'))
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')
```

### 5. Run the bot
After setting the environment variables, you can start the bot by running:
```bash
python bot.py
```

The bot will be up and running, ready to interact with users via Telegram.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
