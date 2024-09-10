import google.generativeai as genai
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Configure the Google Generative AI API using an environment variable
genai.configure(api_key=os.getenv('API_KEY'))
# genai.configure(api_key='AIzaSyDvWEQ5CJzphQ-Ot1mqKMc_ZnEb9P5V-os')

# Initialize the Gemini Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Replace with your Telegram bot token
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')
# TELEGRAM_BOT_TOKEN = '7340913019:AAECZp3me8sUs3PhGAWOQoFsOwgeu3WsWcY'

# Dictionary to store conversation history for each user
conversation_history = {}

async def start(update: Update, context) -> None:
    """Send a message when the command /start is issued."""
    user_id = update.message.from_user.id
    conversation_history[user_id] = []  # Initialize conversation history for the user
    await update.message.reply_text('Hi! I am your Gemini chatbot. Let\'s chat!')

async def handle_message(update: Update, context) -> None:
    """Handle the user's message, maintain conversation context, and respond using the Gemini generative model."""
    user_message = update.message.text
    user_id = update.message.from_user.id
    
    if user_id not in conversation_history:
        conversation_history[user_id] = []  # Initialize history if not started

    # Add the user message to the conversation history
    conversation_history[user_id].append(f"User: {user_message}")

    try:
        # Pass the entire conversation history to the Gemini model for context-aware generation
        full_conversation = "\n".join(conversation_history[user_id])
        response = model.generate_content(full_conversation)
        
        # Add the AI response to the conversation history
        conversation_history[user_id].append(f"{response.text}")
        
        # Send the generated response back to the user
        await update.message.reply_text(response.text)
    
    except Exception as e:
        await update.message.reply_text(f'Error generating response: {e}')

def main():
    """Start the bot."""
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Handle /start command
    application.add_handler(CommandHandler("start", start))
    
    # Handle messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()