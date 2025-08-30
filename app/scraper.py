import time

def scrape_website(url, pages=1, delay=1.5):
    """
    Simulates pagination: returns dummy content for multiple pages.
    """
    results = []
    for i in range(1, pages + 1):
        results.append(f"Content from {url} - Page {i}")
        time.sleep(delay)
    return results
