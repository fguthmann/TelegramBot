import requests


def get_esim_data(country: str):
    try:
        response = requests.get(f"http://127.0.0.1:8000/esim/{country}")
        response.raise_for_status()  # Raises an error for bad responses
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

    if response.status_code == 404:
        return "No eSIM deals found for this country."

    return response.json()
