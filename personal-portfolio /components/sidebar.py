import streamlit as st
import time
import os
from PIL import Image

def render_sidebar():
    with st.sidebar:
        # --- Lock Nav Bar Width ---
        st.markdown("""
            <style>
            /* Lock sidebar width */
            [data-testid="stSidebar"] {
                min-width: 250px !important;
                max-width: 250px !important;
                width: 250px !important;
            }

            /* Hide resizer bar */
            .block-container:has([data-testid="stSidebar"]) + div {
                display: none !important;
            }
            </style>
        """, unsafe_allow_html=True)


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
        st.sidebar.page_link("pages/1_Projects.py", label="📂 Projects")
        st.sidebar.page_link("pages/3_Professional_Development.py", label="🎓 Development")
        st.sidebar.page_link("pages/2_About.py", label="👤 About")
        st.markdown("---")

        # Logo
        
        logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "Futuristic_Tech_Logo.png")
        logo = Image.open(logo_path)
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

        st.markdown("---")

                # --- Handle Session State ---
        if "crash_mode" not in st.session_state:
            st.session_state.crash_mode = False

        # --- Centered Button + Styling ---
        st.markdown("""
            <style>
            .custom-danger-button .stButton > button {
                text-align: center;               
                background-color: #ff0000;
                color: white;
                font-weight: bold;
                font-size: 1rem;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                box-shadow: 0 0 8px red;
                transition: transform 0.1s ease-in-out;
            }
            .custom-danger-button .stButton > button:hover {
                transform: scale(1.05);
                background-color: #cc0000;
            }
            </style>
        """, unsafe_allow_html=True)

        # --- Streamlit Button ---
        with st.sidebar:
                 with st.container():
                    st.markdown('<div class="custom-danger-button">', unsafe_allow_html=True)
                    if st.button("🟥 DO NOT PRESS"):
                        st.session_state.crash_mode = True
                    st.markdown('</div>', unsafe_allow_html=True)

        # --- Redirect if Crash Triggered ---
        if st.session_state.crash_mode:
            st.switch_page("pages/Crash.py")

