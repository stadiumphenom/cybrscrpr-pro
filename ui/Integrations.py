import os
import streamlit as st
import requests

st.markdown("# 🔌 Integrations")

# --- API Key Inputs ---
with st.expander("🔐 Notion"):
    notion_key = st.text_input("Notion API Key", type="password", value=st.session_state.get("NOTION_API_KEY", ""))
    notion_db = st.text_input("Notion Database ID", value=st.session_state.get("NOTION_DATABASE_ID", ""))

with st.expander("📊 Airtable"):
    airtable_key = st.text_input("Airtable API Key", type="password", value=st.session_state.get("AIRTABLE_API_KEY", ""))
    airtable_base = st.text_input("Base ID", value=st.session_state.get("AIRTABLE_BASE_ID", ""))
    airtable_table = st.text_input("Table Name", value=st.session_state.get("AIRTABLE_TABLE", ""))

# --- Save Keys into Session ---
if st.button("💾 Save Keys"):
    st.session_state["NOTION_API_KEY"] = notion_key
    st.session_state["NOTION_DATABASE_ID"] = notion_db
    st.session_state["AIRTABLE_API_KEY"] = airtable_key
    st.session_state["AIRTABLE_BASE_ID"] = airtable_base
    st.session_state["AIRTABLE_TABLE"] = airtable_table
    st.success("🔐 API Keys stored in session.")

# --- Helper: Export to Notion ---
def export_to_notion(content_list):
    if not st.session_state.get("NOTION_API_KEY") or not st.session_state.get("NOTION_DATABASE_ID"):
        st.error("⚠️ Missing Notion credentials")
        return

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {st.session_state['NOTION_API_KEY']}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    for entry in content_list:
        data = {
            "parent": {"database_id": st.session_state["NOTION_DATABASE_ID"]},
            "properties": {
                "Title": {"title": [{"text": {"content": entry.get("url", "No URL")}}]},
                "Content": {"rich_text": [{"text": {"content": entry.get("content", "")[:2000]}}]}
            }
        }
        r = requests.post(url, headers=headers, json=data)
        if r.status_code != 200:
            st.error(f"❌ Notion Error: {r.text}")
        else:
            st.success(f"✅ Sent: {entry.get('url')}")

# --- Helper: Export to Airtable ---
def export_to_airtable(content_list):
    if not st.session_state.get("AIRTABLE_API_KEY") or not st.session_state.get("AIRTABLE_BASE_ID") or not st.session_state.get("AIRTABLE_TABLE"):
        st.error("⚠️ Missing Airtable credentials")
        return

    url = f"https://api.airtable.com/v0/{st.session_state['AIRTABLE_BASE_ID']}/{st.session_state['AIRTABLE_TABLE']}"
    headers = {"Authorization": f"Bearer {st.session_state['AIRTABLE_API_KEY']}", "Content-Type": "application/json"}

    for entry in content_list:
        data = {
            "fields": {
                "URL": entry.get("url", ""),
                "Content": entry.get("content", "")[:2000],
                "Page": entry.get("page", 1)
            }
        }
        r = requests.post(url, headers=headers, json=data)
        if r.status_code not in (200, 201):
            st.error(f"❌ Airtable Error: {r.text}")
        else:
            st.success(f"✅ Sent: {entry.get('url')}")

# --- UI to trigger exports (only if scrape results exist) ---
if "last_results" in st.session_state and st.session_state["last_results"]:
    st.markdown("## 📤 Export Scraped Results")

    if st.button("🚀 Send to Notion"):
        export_to_notion(st.session_state["last_results"])

    if st.button("🚀 Send to Airtable"):
        export_to_airtable(st.session_state["last_results"])
else:
    st.info("⚠️ No scraped results found in session. Go scrape something first on the Home page.")
