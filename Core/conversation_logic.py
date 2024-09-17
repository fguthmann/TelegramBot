from telegram import Update
from telegram.ext import ContextTypes
from Backend.client_api import get_esim_data
import pycountry


async def main_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()

    if message_text == '/start':
        await update.message.reply_text('Welcome! To start searching for eSIM deals, please tell me the country.')
        # Clear any previous conversation data
        context.user_data.clear()
        return

    if 'country' not in context.user_data:
        return await handle_ask_country(update, context)
    elif 'days' not in context.user_data:
        return await handle_ask_days(update, context)
    elif 'gb' not in context.user_data:
        return await handle_ask_gb(update, context)


async def handle_ask_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text.capitalize()

    # Validate the country input using pycountry
    if not pycountry.countries.get(name=country):
        await update.message.reply_text("This doesn't seem to be a valid country. Please enter a valid country name.")
        return

    context.user_data['country'] = country
    await update.message.reply_text(f"Great! You entered {country}. How many days will you be staying?")


async def handle_ask_days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        days = int(update.message.text)
        if days <= 0:
            raise ValueError

        context.user_data['days'] = days
        await update.message.reply_text("Awesome! How many GB of data do you need?")
    except ValueError:
        await update.message.reply_text("Please enter a valid number of days.")


async def handle_ask_gb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        gb = float(update.message.text)
        if gb <= 0:
            raise ValueError

        country = context.user_data['country']
        days = context.user_data['days']
        context.user_data['gb'] = gb

        esim_data = get_esim_data(country, days, gb)

        # Error or "No eSIM found" message
        if isinstance(esim_data, str):
            await update.message.reply_text(esim_data)
        else:
            esim_list = "\n".join([f"Provider: {esim['provider']}, Price: {esim['price']}, Days: {esim['days']}, "
                                   f"GB: {esim['gb']}" for esim in esim_data])
            await update.message.reply_text(f"Here are the best eSIM deals:\n{esim_list}")

    except ValueError:
        await update.message.reply_text("Please enter a valid number of GB.")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Goodbye! If you need help again, just ask!")
    context.user_data.clear()
