import requests
from Core.esim_utils import sort_esims_by_prices
import os
from dotenv import load_dotenv

load_dotenv()
FASTAPI_URL = os.getenv("FASTAPI_URL")


def get_esim_data(country: str, min_days: int, min_gb: float):
    try:
        response = requests.get(f"{FASTAPI_URL}/esim/{country}", params={"min_days": min_days, "min_gb": min_gb})
        response.raise_for_status()  # Raises an error for bad responses
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

    if response.status_code == 404:
        return "No eSIM deals found for this country."
    esims = response.json()

    sorted_esims = sort_esims_by_prices(esims)
    return sorted_esims
