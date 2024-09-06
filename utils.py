import requests


def get_today_date():
    response = requests.get("http://127.0.0.1:8000/get_date").json()
    return response["date"]


def generate_response(user_input: str) -> str:
    # Custom logic for response generation
    normalized_input: str = user_input.lower()

    if 'what is the date' in normalized_input:
        return get_today_date()

    return 'I didn’t catch that, could you please rephrase?'

