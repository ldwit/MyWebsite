import streamlit as st
import time
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")
apply_global_styles()
render_sidebar()

# --- Header ---
st.markdown(
    """
    <style>
    .hero-text {
        font-size: 2rem;
        font-weight: 600;
        color: #00FFF7;
        margin-bottom: 0.5rem;
    }
    .quote {
        font-style: italic;
        font-size: 1.2rem;
        color: #AAAAAA;
    }
    </style>
    <div class="hero-text">👋 Welcome! Thank you for visiting!</div><br>
    <div class="quote">
        “Tell me and I forget, teach me and I may remember, involve me and I learn.” <br>
        — Benjamin Franklin
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Featured Projects Section ---
st.markdown("### 🌟 Featured Projects")

# Use columns to display 4 projects
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("https://images.unsplash.com/photo-1630260667842-830a17d12ec9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=155)
    st.markdown("**Weather Dashboard**")
    st.caption("Real-time weather data collection using Python, S3, and OpenWeather API.")
    st.page_link("pages/WeatherDashboardDemo.py", label="🔗 View Project", icon="🌦️")

with col2:
    st.image("https://plus.unsplash.com/premium_vector-1715081572707-7ad0ab66a6ca?q=80&w=2360&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=100)
    st.markdown("**Okta SSO Integration**")
    st.caption("Configured SAML SSO between Okta and ServiceNow.")
    st.page_link("pages/OktaAppIntegration_ServiceNow.py", label="🔗 View Project", icon="🔐")

with col3:
    st.image("https://images.unsplash.com/vector-1739953047277-154ad3a57890?q=80&w=2360&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=100)
    st.markdown("**GCP AD Setup**")
    st.caption("Provisioned a Windows Server VM on GCP and configured Active Directory.")
    st.page_link("pages/GCPVM_AD.py", label="🔗 View Project", icon="🖥️")

with col4:
    st.image("https://plus.unsplash.com/premium_vector-1726040467797-7595261075e4?q=80&w=2360&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=100)
    st.markdown("**Band Name Generator**")
    st.caption("A fun Python Streamlit app combining city and pet names.")
    st.page_link("pages/BandNameGeneratorApp.py", label="🔗 View Project", icon="🎸")

st.markdown("---")

# --- Optional Footer or Call-to-Action ---
st.markdown("### 💡 Explore More")
st.page_link("pages/1_Projects.py", label="🧰 Browse All Projects", icon="🧰")
