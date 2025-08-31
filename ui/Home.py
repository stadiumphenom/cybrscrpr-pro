import streamlit as st

st.set_page_config(page_title="CYBRSCRPR-Pro", layout="wide")
import random

emoji_themes = ["🎭", "🤖", "🧠", "🕵️", "📡", "💾", "💣", "⚡", "👾"]
chosen_emoji = random.choice(emoji_themes)

st.markdown(f"<h1 style='text-align: center;'>{chosen_emoji} CYBRSCRPR-Pro {chosen_emoji}</h1>", unsafe_allow_html=True)

# --- Animated CSS UI ---
st.markdown("""
    <style>
    /* Matrix Rain Background */
    body::before {
        content: "01 10 11 00 01 01 10 01 00 01 11 10 00 01 10";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        font-family: monospace;
        font-size: 12px;
        color: rgba(0, 255, 0, 0.15);
        z-index: -1;
        animation: matrixRain 5s linear infinite;
        white-space: pre;
    }

    @keyframes matrixRain {
        0% { transform: translateY(-100%) rotate(0deg); }
        100% { transform: translateY(100%) rotate(360deg); }
    }

    /* Text Areas */
    textarea {
        background-color: #0d0d0d !important;
        color: #00FF00 !important;
        font-family: monospace !important;
        border: 1px solid #333 !important;
    }

    /* Spinner text */
    .stSpinner > div > div {
        color: #00FF00 !important;
        font-weight: bold;
        font-family: monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🚀 CYBRSCRPR-Pro")
st.markdown("Navigate using the sidebar.")
