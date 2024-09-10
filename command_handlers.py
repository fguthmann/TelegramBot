from telegram import Update
from telegram.ext import ContextTypes
from states import ASK_COUNTRY


async def initiate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome! To start searching for eSIM deals, please tell me the country.')
    return ASK_COUNTRY  # Start the conversation


async def assist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is the help message. You can start by typing /start to search for eSIM deals.')


async def personalize_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command response.')
