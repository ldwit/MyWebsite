import streamlit as st
from components.sidebar import render_sidebar

# --- Page config ---
st.set_page_config(page_title="LT Portfolio", page_icon="📁", layout="wide")

# --- Render the sidebar (shared layout) ---
render_sidebar()

# --- Main content ---
st.title("👋 Welcome to My Project Portfolio")
st.write("Explore my work, skills, and more — all powered by Python + Streamlit.")