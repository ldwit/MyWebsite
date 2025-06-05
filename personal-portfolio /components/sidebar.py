import streamlit as st
from PIL import Image

def render_sidebar():
    with st.sidebar:
        # Logo
        logo = Image.open("assets/Futuristic_Tech_Logo.png")
        st.image(logo, use_container_width=True)

        # Nav Header
        st.markdown("## 📂 Navigation")
        st.markdown("---")

        # Footer
        st.markdown(
            """
            <div style='text-align: center; font-size: 14px; margin-top: 2rem;'>
                Made with <img src='https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg' 
                width='20' style='vertical-align: middle;'/> by LT
            </div>
            """,
            unsafe_allow_html=True
        )
