import streamlit as st
from PIL import Image


# --- Load PNG image ---
logo_image = Image.open("assets/Futuristic_Tech_Logo.png")

# --- Sidebar Layout ---
with st.sidebar:
    # Display PNG logo at top
    st.image(logo_image, width=200)

    st.markdown("## Navigation")
    selected_page = st.radio("Choose a page:", ["Home", "Loading"])

    st.markdown("---")

    st.markdown(
        """
        <div style="display: flex; align-items: center;">            
            <span>Made with <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" width="30"> by LT</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Page Router ---
if selected_page == "Home":
    st.switch_page("webpages/home.py")
elif selected_page == "Loading":
    st.switch_page("webpages/loading_page.py")