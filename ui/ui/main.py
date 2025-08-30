
import streamlit as st
import pandas as pd
from app import exporter

st.set_page_config(page_title="CYBRSCRPR-Pro", layout="wide")
st.title("🕵️ CYBRSCRPR-Pro – Export Edition")

data = [
    {"url": "https://example.com", "title": "Example", "text": "Sample text", "email": "test@example.com"},
    {"url": "https://foo.com", "title": "Foo", "text": "Foo content", "email": "contact@foo.com"},
]

df = pd.DataFrame(data)
st.dataframe(df)

st.markdown("### 📤 Export Options")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Download CSV"):
        filename = exporter.export_csv(data)
        st.success(f"CSV exported as {filename}")

with col2:
    if st.button("Download JSON"):
        filename = exporter.export_json(data)
        st.success(f"JSON exported as {filename}")

with col3:
    if st.button("Download Excel"):
        filename = exporter.export_excel(data)
        st.success(f"Excel exported as {filename}")
