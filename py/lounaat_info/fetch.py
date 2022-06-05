# contents of app.py, a simple API retrieval example
import requests


# https://www.lounaat.info/ajax/filter?view=lahistolla&day=11&page=0&coords%5Blat%5D=64.24803849999999&coords%5Blng%5D=27.7996717&coords%5Baddress%5D=87250-kajaani&coords%5BformattedAddress%5D=87250%20Kajaani


def fetch_lunch_data(day, lat, lon) -> str:
    """Takes a URL, and returns the text."""
    url = f"https://www.lounaat.info/ajax/filter?view=lahistolla&day={day}&page=0&coords%5Blat%5D={lat}&coords%5Blng%5D={lon}&coords%5Baddress%5D=87250-kajaani&coords%5BformattedAddress%5D=87250%20Kajaani"
    r = requests.get(url, headers={"referer": "https://www.lounaat.info"})
    return r
