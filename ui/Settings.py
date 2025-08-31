import streamlit as st
import pyttsx3
import os
import pathlib

st.markdown("# ⚙️ Settings & Voice")

# --- Theme Switcher ---
theme = st.radio("Select Theme", ["Dark", "Light"], index=0)
if theme == "Dark":
    st.session_state["theme"] = "dark"
else:
    st.session_state["theme"] = "light"

st.info("ℹ️ Themes are primarily configured via `.streamlit/config.toml`. \
The switch here just sets a session preference for dynamic styling.")

st.success(f"Current Theme: {st.session_state['theme']}")

# --- Voice Settings ---
st.markdown("## 🔊 Voice Assistant")
voice_text = st.text_input("Enter text to speak:", "Welcome back to CYBRSCRPR-Pro. Let's extract the web.")

if st.button("▶️ Speak"):
    try:
        engine = pyttsx3.init()

        # Optional voice customization
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)  # pick first available voice
        engine.setProperty('rate', 165)  # slower speed for clarity

        engine.say(voice_text)
        engine.runAndWait()
        st.success("✅ Voice played successfully.")
    except Exception as e:
        st.error(f"❌ Voice playback failed: {e}")

# --- Reset / Clear Keys ---
st.markdown("## 🧹 Reset Credentials")
if st.button("Clear Saved API Keys"):
    for key in ["NOTION_API_KEY", "NOTION_DATABASE_ID",
                "AIRTABLE_API_KEY", "AIRTABLE_BASE_ID", "AIRTABLE_TABLE"]:
        if key in st.session_state:
            del st.session_state[key]
    st.success("🔐 API keys cleared from session.")

# --- Debug Info (optional) ---
with st.expander("🐛 Debug Info"):
    st.json({k: str(v) for k, v in st.session_state.items()})
