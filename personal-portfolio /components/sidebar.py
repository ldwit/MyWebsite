import streamlit as st
from PIL import Image

def render_sidebar():
    with st.sidebar:
        # Hide default sidebar page navigation
        st.markdown("""
            <style>
            [data-testid="stSidebarNav"] {
                width: 100px !important;
                min-width: 100px !important;
                max-width: 100px !important;
                display: none;                
            }
            </style>
            """, unsafe_allow_html=True)

        # --- Your custom sidebar content below ---
        # st.sidebar.title("🔍 Navigation")
        st.sidebar.page_link("pages/Home.py", label="🏠 Home")
        st.sidebar.page_link("/workspaces/MyWebsite/personal-portfolio /pages/1_Projects.py", label="📂 Projects")
        st.sidebar.page_link("/workspaces/MyWebsite/personal-portfolio /pages/3_Professional_Development.py", label="🎓 Development")
        st.sidebar.page_link("/workspaces/MyWebsite/personal-portfolio /pages/2_About.py", label="👤 About")
        st.markdown("---")

        # Logo
        logo = Image.open("assets/Futuristic_Tech_Logo.png")
        st.image(logo, use_container_width=True)

        st.markdown("### 🌐 Connect With Me")

        st.markdown(
            """
            <div style='text-align: center;'>
                <a href="https://www.linkedin.com/in/ldwit/" target="_blank" style="margin-right: 15px;">
                    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" width="24" style="filter: invert(100%);">
                </a>
                <a href="https://dev.to/ldwit" target="_blank" style="margin-right: 15px;">
                    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/devdotto.svg" width="24" style="filter: invert(100%);">
                </a>
                <a href="https://github.com/ldwit" target="_blank">
                    <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" width="24" style="filter: invert(100%);">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown("---")

        # Footer
        st.markdown(
            """
            <div style='text-align: center; font-size: 18px; margin-top: 2rem;'>
                Made with <img src='https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg' 
                width='10' style='width: 18px; height: 18px; vertical-align: middle;'/> by LT
            </div>
            """,
            unsafe_allow_html=True
        )
