from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
import os
from dotenv import load_dotenv
from command_handlers import initiate_command, assist_command, personalize_command
from conversation_logic import ask_country, ask_days, ask_gb, cancel
from error_handling import log_error
from states import ASK_COUNTRY, ASK_DAYS, ASK_GB

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')


def start_bot():
    app = Application.builder().token(API_TOKEN).build()

    # Define the conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', initiate_command)],  # Conversation starts with /start
        states={
            ASK_COUNTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_country)],  # Handle country input
            ASK_DAYS: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_days)],  # Handle days input
            ASK_GB: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_gb)],  # Handle GB input
        },
        fallbacks=[CommandHandler('cancel', cancel)]  # Handle cancellation
    )

    # Add the conversation handler
    app.add_handler(conv_handler)

    # Register additional command handlers
    app.add_handler(CommandHandler('help', assist_command))
    app.add_handler(CommandHandler('custom', personalize_command))

    # Register error handler
    app.add_error_handler(log_error)

    # Start polling
    print('Starting polling...')
    app.run_polling(poll_interval=2)
