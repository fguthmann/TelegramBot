from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv
from command_handlers import initiate_command, assist_command, personalize_command
from message_processing import process_message
from error_handling import log_error

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')


def start_bot():
    app = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', initiate_command))
    app.add_handler(CommandHandler('help', assist_command))
    app.add_handler(CommandHandler('custom', personalize_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, process_message))

    # Register error handler
    app.add_error_handler(log_error)

    print('Starting polling...')
    # Run the bot
    app.run_polling(poll_interval=2)
