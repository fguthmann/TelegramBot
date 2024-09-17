from telegram import Update
from telegram.ext import ContextTypes
from Core.conversation_logic import main_conversation


async def initiate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await main_conversation(update, context)
