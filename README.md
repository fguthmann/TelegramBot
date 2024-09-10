# TelegramBot

## Setting Up the Telegram Bot

### 1. Install Dependencies
First, you need to install the `python-telegram-bot` library. Run the following command in your terminal:

```bash
pip install python-telegram-bot
```
You need to install the `pycountry` library. Run the following command in your terminal:
```bash
pip install pycountry
```

### 2. Create a Bot Token
To create a bot on Telegram and get your token, follow these steps:

1. Open Telegram and search for **BotFather** in the search bar.
2. Start a conversation by pressing the `/start` button.
3. Create a new bot by typing `/newbot` or selecting the `/newbot` option.
4. Name your bot when prompted. This will be the display name of your bot.
5. Choose a **unique** username for your bot, which must end with the word **bot** (e.g., `my_bot`).
6. After completing these steps, you will receive your **HTTP API Token**. This is your bot's authentication token.

    - **API_TOKEN**: The token you received from BotFather.
    - **BOT_HANDLE**: The username you created for your bot.

### 3. Set Up Date API
To handle date queries, make sure you download and set up the **DateAPI** as a microservice that works alongside your bot.

### 4. You're Ready to Start!
Once everything is set up, you can start your bot and Date API and begin interacting with your Telegram bot.
