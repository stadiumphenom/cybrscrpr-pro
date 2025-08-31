# app/scraper.py
import time
import requests
from app.parser import parse_html

def scrape(url, pages=1, delay=1.5):
    results = []

    for page_num in range(1, pages + 1):
        try:
            # This assumes static URLs, not paginated ones like ?page=2 etc.
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                parsed_content = parse_html(response.text)
                combined_text = "\n".join(parsed_content)

                results.append({
                    "url": url,
                    "page": page_num,
                    "content": combined_text
                })
            else:
                results.append({
                    "url": url,
                    "page": page_num,
                    "content": f"❌ Failed with status code {response.status_code}"
                })
        except Exception as e:
            results.append({
                "url": url,
                "page": page_num,
                "content": f"❌ Error scraping page {page_num}: {e}"
            })

        time.sleep(delay)

    return results
