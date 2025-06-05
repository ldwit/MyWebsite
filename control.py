import streamlit as st
from PIL import Image

# --- Load the image ---
logo_image = Image.open("assets/Futuristic_Tech_Logo.png")

# --- Sidebar Content ---
with st.sidebar:
    # Display the logo at the very top
    st.image(logo_image, width=200)

    # Navigation section
    st.markdown("## Navigation")
    selected_page = st.radio("Choose a page:", ["Home", "Loading"])

    st.markdown("---")

    # Footer / Signature
    st.markdown(
        """
        <div style="display: flex; align-items: center;">            
            <span>Made with <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" width="30"> by LT</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Routing Logic ---
if selected_page == "Home":
    st.switch_page("Home")  # Assumes pages/Home.py exists
elif selected_page == "Loading":
    st.switch_page("Loading")  # Assumes pages/Loading.py exists
