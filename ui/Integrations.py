import streamlit as st

st.markdown("# 🔌 Integrations")

with st.expander("🔐 Notion"):
    notion_key = st.text_input("Notion API Key", type="password")
    notion_db = st.text_input("Notion Database ID")

with st.expander("📊 Airtable"):
    airtable_key = st.text_input("Airtable API Key", type="password")
    airtable_base = st.text_input("Base ID")
    airtable_table = st.text_input("Table Name")

if st.button("💾 Save Keys"):
    st.session_state["NOTION_API_KEY"] = notion_key
    st.session_state["NOTION_DATABASE_ID"] = notion_db
    st.session_state["AIRTABLE_API_KEY"] = airtable_key
    st.session_state["AIRTABLE_BASE_ID"] = airtable_base
    st.session_state["AIRTABLE_TABLE"] = airtable_table
    st.success("🔐 API Keys stored in session.")
