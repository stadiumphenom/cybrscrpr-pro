import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import openai
import os
import json
import pandas as pd
from app.scraper import scrape_website
from app.filters import filter_results

# Page setup
st.set_page_config(page_title="CYBRSCRPR-Pro", layout="wide")
st.title("🕵️ CYBRSCRPR-Pro - Web Content Scraper")

# User input
url_input = st.text_area("Enter URLs to Scrape (one per line):", height=100)
pages = st.number_input("Pages per URL:", min_value=1, value=3)
delay = st.number_input("Delay between pages (seconds):", min_value=0.0, value=1.5)
keywords_input = st.text_input("Filter by Keywords (comma-separated, optional):")
use_openai = st.checkbox("Use OpenAI to summarize content", value=True)

# Scrape action
if st.button("🚀 Scrape Data"):
    urls = [url.strip() for url in url_input.strip().splitlines() if url.strip()]
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

    if not urls:
        st.error("Please enter at least one valid URL.")
    else:
        all_results = []

        for url in urls:
            with st.spinner(f"Scraping {url} over {pages} page(s)..."):
                try:
                    scraped = scrape_website(url, pages=pages, delay=delay)

                    if keywords:
                        scraped = filter_results(scraped, keywords)

                    for item in scraped:
                        all_results.append({"url": url, "content": item})

                except Exception as e:
                    st.error(f"Error scraping {url}: {e}")

        if all_results:
            st.success(f"✅ Scraped {len(all_results)} items total.")

            # Display results
            for i, entry in enumerate(all_results, 1):
                st.markdown(f"**{i}.** `{entry['url']}`\n\n{entry['content']}")

            # Auto-export to CSV
            df = pd.DataFrame(all_results)

            # Create CSV and JSON in memory
            csv_data = df.to_csv(index=False).encode('utf-8')
            json_data = json.dumps(all_results, indent=2).encode('utf-8')

            st.subheader("📦 Download Results")
            st.download_button("⬇️ Download CSV", data=csv_data, file_name="scraped_results.csv", mime="text/csv")
            st.download_button("⬇️ Download JSON", data=json_data, file_name="scraped_results.json", mime="application/json")

            # Optional: Summarize via OpenAI
            if use_openai:
                openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
                if not openai.api_key:
                    st.warning("OpenAI API key is missing.")
                else:
                    with st.spinner("Generating summary with OpenAI..."):
                        try:
                            full_text = "\n".join([entry['content'] for entry in all_results])[:3500]
                            response = openai.ChatCompletion.create(
                                model="gpt-3.5-turbo",
                                messages=[{
                                    "role": "user",
                                    "content": f"Summarize the following web content:\n{full_text}"
                                }]
                            )
                            summary = response.choices[0].message.content
                            st.subheader("📝 OpenAI Summary")
                            st.success(summary)
                        except Exception as e:
                            st.error(f"OpenAI Error: {e}")
        else:
            st.warning("No results found.")
