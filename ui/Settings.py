import streamlit as st
import pyttsx3

st.markdown("# ⚙️ Settings & Voice")

theme = st.radio("Select Theme", ["Dark", "Light"], index=0)
st.success(f"Selected: {theme} (change via `.streamlit/config.toml`)")

if st.button("🔊 Speak Welcome"):
    engine = pyttsx3.init()
    engine.say("Welcome back to CYBRSCRPR-Pro. Let's extract the web.")
    engine.runAndWait()
