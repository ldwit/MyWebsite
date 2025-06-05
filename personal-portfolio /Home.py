import streamlit as st
from components.sidebar import render_sidebar

# --- Page config ---
st.set_page_config(page_title="LT Portfolio", page_icon="📁", layout="wide")


# --- Page Font ---

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Render the sidebar (shared layout) ---
render_sidebar()

# --- Main content ---
st.title("👋 Welcome to My Project Portfolio")
st.write("Explore my work, skills, and more — all powered by Python + Streamlit.")