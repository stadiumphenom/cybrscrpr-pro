import sys
import os
import json
import pandas as pd
import streamlit as st
import openai

# Set up import path and Streamlit config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
st.set_page_config(page_title="CYBRSCRPR-Pro", layout="wide")
st.title("🕵️ CYBRSCRPR-Pro - Web Content Scraper")

# Internal modules
from app.scraper import scrape
from app.filters import filter_results
from app.exporter import export_to_csv, export_to_json, export_to_excel

# --- User Inputs ---
url_input = st.text_area("Enter URLs to Scrape (one per line):", height=100)
pages = st.number_input("Pages per URL:", min_value=1, value=3)
delay = st.number_input("Delay between pages (seconds):", min_value=0.0, value=1.5)
keywords_input = st.text_input("Filter by Keywords (comma-separated, optional):")
use_openai = st.checkbox("Use OpenAI to summarize content", value=True)

# --- Action Button ---
if st.button("🚀 Scrape Data"):
    urls = [url.strip() for url in url_input.strip().splitlines() if url.strip()]
    keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]
    all_results = []

    if not urls:
        st.error("Please enter at least one valid URL.")
    else:
        for url in urls:
            with st.spinner(f"Scraping {url} over {pages} page(s)..."):
                try:
                    scraped = scrape(url, pages=pages, delay=delay)

                    if keywords:
                        scraped = filter_results(scraped, keywords)

                    all_results.extend(scraped)

                except Exception as e:
                    st.error(f"Error scraping {url}: {e}")

        if all_results:
            st.success(f"✅ Scraped {len(all_results)} items total.")

            # --- Display Results ---
            for i, entry in enumerate(all_results, 1):
                st.markdown(f"### 🔗 Page {entry.get('page', i)} — [{entry['url']}]({entry['url']})")
                st.text_area("📄 Parsed Content", entry["content"], height=250)

            # --- Export & Download ---
            st.subheader("📦 Download Results")
            df = pd.DataFrame(all_results)

            csv_file = export_to_csv(all_results)
            json_file = export_to_json(all_results)
            excel_file = export_to_excel(all_results)

            with open(csv_file, "rb") as f:
                st.download_button("⬇️ Download CSV", f, file_name=os.path.basename(csv_file), mime="text/csv")

            with open(json_file, "rb") as f:
                st.download_button("⬇️ Download JSON", f, file_name=os.path.basename(json_file), mime="application/json")

            with open(excel_file, "rb") as f:
                st.download_button("⬇️ Download Excel", f, file_name=os.path.basename(excel_file), mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

            # --- Optional: OpenAI Summary ---
            if use_openai:
                openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
                if not openai.api_key:
                    st.warning("OpenAI API key is missing.")
                else:
                    with st.spinner("Generating summary with OpenAI..."):
                        try:
                            full_text = "\n".join(entry["content"] for entry in all_results)[:3500]
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
