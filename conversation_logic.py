import pycountry
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from states import ASK_COUNTRY, ASK_DAYS, ASK_GB
from api_client import get_esim_data


async def ask_country(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text
    print(f"Received country input: {country}")

    # Validate the country input using pycountry
    if not pycountry.countries.get(name=country):
        await update.message.reply_text("This doesn't seem to be a valid country. Please enter a valid country name.")
        return ASK_COUNTRY  # Stay on this state if invalid country

    # Store the country in user data
    context.user_data['country'] = country

    # Proceed to the next step: ask for number of days
    await update.message.reply_text(f"Great! You entered {country}. How many days will you be staying?")
    return ASK_DAYS


async def ask_days(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        days = int(update.message.text)
        if days <= 0:
            raise ValueError

        # Store the days in user data
        context.user_data['days'] = days

        # Ask for GB of data
        await update.message.reply_text("Awesome! How many GB of data do you need?")
        return ASK_GB
    except ValueError:
        await update.message.reply_text("Please enter a valid number of days.")
        return ASK_DAYS


async def ask_gb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        gb = float(update.message.text)
        if gb <= 0:
            raise ValueError

        # Store the GB in user data
        context.user_data['gb'] = gb

        # Get the country, days, and GB from the user data
        country = context.user_data['country']
        days = context.user_data['days']
        gb = context.user_data['gb']

        # Fetch eSIM data from the API
        esim_data = get_esim_data(country)

        # Respond with the eSIM data
        await update.message.reply_text(
            f"Looking for the best eSIM deal for {country} for {days} days with {gb}GB of data...\n{esim_data}"
        )

        # End the conversation after providing the response
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Please enter a valid number of GB.")
        return ASK_GB


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Goodbye! If you need help again, just ask!")
    return ConversationHandler.END
