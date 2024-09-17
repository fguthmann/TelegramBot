from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from Bot.command_handlers import initiate_command
from Core.conversation_logic import main_conversation, cancel
from Core.error_handling import log_error

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


def start_bot():
    app = Application.builder().token(API_TOKEN).build()

    # Add the conversation handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, main_conversation))

    # Register command handlers
    app.add_handler(CommandHandler('start', initiate_command))
    app.add_handler(CommandHandler('cancel', cancel))

    # Register error handler
    app.add_error_handler(log_error)

    # Start polling
    print('Starting polling...')
    app.run_polling(poll_interval=2)
