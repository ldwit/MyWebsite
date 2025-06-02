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

# -- Navigation Setup [With Sections] --

pg = st.navigation(
    {
        "Loading": [loading_page],
        "Home": [home],
    }
)


# -- Run Navigation --

pg.run()