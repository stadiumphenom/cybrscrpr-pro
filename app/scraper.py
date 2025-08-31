import requests
from bs4 import BeautifulSoup

def scrape_website(url, pages=1, delay=1.5):
    all_text = []

    for _ in range(pages):
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Try to extract main content
            paragraphs = soup.find_all("p")
            page_text = " ".join(p.get_text(strip=True) for p in paragraphs)

            if page_text:
                all_text.append(page_text)
            else:
                all_text.append("⚠️ No <p> tags found.")

        except Exception as e:
            all_text.append(f"❌ Error scraping {url}: {str(e)}")

    return all_text
