import streamlit as st

st.markdown("# 📝 Summary")

# Check if summaries exist in session
if "last_summary" in st.session_state and st.session_state["last_summary"]:
    st.success("✅ Found a summary generated on the Home page.")
    st.markdown("### 📄 AI Summary")
    st.write(st.session_state["last_summary"])

elif "last_results" in st.session_state and st.session_state["last_results"]:
    st.warning("⚠️ No summary yet, but scraped results are available.")
    st.markdown("👉 Go back to **Home** and click the `Use OpenAI to summarize` option.")
else:
    st.info("No summaries available yet. Run a scrape with summarization on the Home page.")
