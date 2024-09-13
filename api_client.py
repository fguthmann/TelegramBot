import requests
from esim_filters import filter_esims_by_criteria


def get_esim_data(country: str, min_days: int, min_gb: float):
    try:
        response = requests.get(f"http://127.0.0.1:8000/esim/{country}")
        response.raise_for_status()  # Raises an error for bad responses
    except requests.exceptions.RequestException as e:
        return f"Error occurred: {e}"

    if response.status_code == 404:
        return "No eSIM deals found for this country."
    esims = response.json()

    # Filter eSIMs based on min_days and min_gb if provided
    filtered_esims = filter_esims_by_criteria(esims, min_days, min_gb)

    return filtered_esims
