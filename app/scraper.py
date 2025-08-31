from playwright.sync_api import sync_playwright
import time

def scrape_website(url, pages=1, delay=1.5):
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for i in range(pages):
            try:
                page.goto(url, timeout=15000)
                page.wait_for_timeout(delay * 1000)

                # Extract visible text from <body>
                content = page.locator("body").inner_text()
                text = content.strip()[:5000]

                results.append(f"📄 Content from {url} — Page {i + 1}\n\n{text}")
            except Exception as e:
                results.append(f"❌ Error on page {i+1}: {e}")

        browser.close()

    return results
