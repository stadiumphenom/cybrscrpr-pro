import requests
from parser import parse_html

def scrape_website(url):
    """
    Fetches a URL and extracts structured + readable content.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return parse_html(response.text)
