# eSim Search TelegramBot

## Overview

This Telegram bot allows users to search for eSIM deals based on country, duration (days), and data requirements (GB).
The bot interacts with a FastAPI backend, which queries a MongoDB database to provide relevant eSIM options. Users can
interact with the bot to specify their criteria, and it will return a list of suitable eSIM deals sorted by price.



## Setting Up the Telegram Bot

### 1. Install Dependencies
First, ensure you have python 3.8 or higher installed. Installed the required dependencies:

-`python-telegram-bot`  
-`pycountry`  
-`fastapi`  
-`uvicorn`  
-`pymongo`  
-`requests`  
-`python-dotenv`  

Run the following command in your terminal:

```bash
pip install python-telegram-bot pycountry fastapi uvicorn pymongo requests python-dotenv

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

### 3. Set Up Environment Variables:
Create a `.env` file in the root of your project and add the following variables:
``` bash 
API_TOKEN=your_telegram_bot_api_token
BOT_HANDLE= @your_telegram_bot_username
FASTAPI_URL=http://localhost:8000
DB_ADDRESS=your_mongodb_connection_string
```

### 4. Set Up the FastAPI Backend

Start the FastAPI server to handle requests from the bot:
``` bash 
uvicorn app:app --reload
```
This will start the FastAPI server on http://localhost:8000 by default.

### 5. Start the Telegram Bot
Once everything is set up, start your Telegram bot by running:

``` bash 
python main.py
```
### 6. Interact with the Bot
You can now interact with your bot on Telegram. Simply start a conversation with your bot's username and follow the 
prompts to search for eSIM deals.