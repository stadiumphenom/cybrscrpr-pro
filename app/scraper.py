import time
import requests
from bs4 import BeautifulSoup

def scrape_website(url, pages=1, delay=1.5):
    all_results = []

    for page_num in range(pages):
        try:
            print(f"Scraping {url} (Page {page_num + 1})")
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # 🧠 Try to extract useful visible text
            main = soup.find("main") or soup.find("div", {"id": "content"}) or soup
            paragraphs = main.find_all("p")
            text = "\n".join(p.get_text(strip=True) for p in paragraphs)

            if not text.strip():
                text = soup.get_text(strip=True)[:2000]  # Fallback: raw text

            result = f"Content from {url} — Page {page_num + 1}\n\n{text}"
            all_results.append(result)

            time.sleep(delay)

        except Exception as e:
            error_message = f"❌ Error scraping {url}: {str(e)}"
            all_results.append(error_message)

    return all_results
