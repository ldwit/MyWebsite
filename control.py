from PIL import Image
import streamlit as st

# --- Page Setup ---
loading_page = st.Page(
    page="webpages/loading_page.py",
    title="Loading Page",
    icon=":material/iframe:",
    default=True,
)

home = st.Page(
    page="webpages/home.py",
    title="Home",
    icon=":material/home:",
)

# --- Sidebar Content (Grouped at the Top) ---
with st.sidebar:
    # Display the logo image at the very top
    # --- Force image position ---

    st.markdown(
        """
        <style>
        .sidebar-top-logo {
            position: fixed;
            top: 1rem;
            left: 1rem;
            width: 220px;
            z-index: 1001;
        }
        .block-container {
            padding-top: 6rem;  /* Push main content down so it doesn't clash */
        }
        </style>

        <div class="sidebar-top-logo">
            <img src="assets/LDWIT.gif" width="200" />
        </div>
        """,
        unsafe_allow_html=True
    )

    # Spacer or additional elements if needed
    st.markdown("---")

    # Footer or credit message
    st.markdown(
        """
        <div style="display: flex; align-items: center;">            
            <span>Made with <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" width="30"> by LT</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Navigation Setup [With Sections] ---
pg = st.navigation(
    {
        "Loading": [loading_page],
        "Home": [home],
    }
)

# --- Run Navigation ---
pg.run()
