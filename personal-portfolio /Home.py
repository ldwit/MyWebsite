import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

st.set_page_config(page_title="Home", page_icon="🧿", layout="wide")

# Apply styles globally
apply_global_styles()

render_sidebar()

st.title("👋 Welcome to My Project Portfolio")
st.write("Explore my work, skills, and more... All powered by Python + Streamlit.")
