import requests
import difflib


def get_today_date():
    response = requests.get("http://127.0.0.1:8000/get_date").json()
    return response["date"]


def generate_response(user_input: str) -> str:
    # Custom logic for response generation
    normalized_input: str = user_input.lower()

    # List of possible valid commands
    valid_phrases = ['what is the date', 'tell me the date', 'date today']

    # Find the closest match to the user's input
    match = difflib.get_close_matches(normalized_input, valid_phrases, n=1, cutoff=0.6)

    if match:
        return get_today_date()

    return 'I didn’t catch that, could you please rephrase?'

