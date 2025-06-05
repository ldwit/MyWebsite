import streamlit as st

def apply_global_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');

        html, body, [class*="css"] {
            font-family: 'Audiowide', sans-serif !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
