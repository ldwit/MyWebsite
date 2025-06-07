import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Apply styles globally
apply_global_styles()

render_sidebar()

st.markdown(
    """
    <style>
    .typewriter h2 {
      font-size: 28px;
      font-family: "Audiowide", sans-serif;
      color: #00FFF7;
      overflow: hidden;
      border-right: .15em solid #00FFF7;
      white-space: nowrap;
      margin: 0 auto;
      letter-spacing: .05em;
      animation: typing 3.5s steps(40, end), blink-caret .75s step-end infinite;
    }

    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }

    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: #00FFF7; }
    }
    </style>

    <div class="typewriter">
      <h2>🖥️ Initializing Profile... ✅ Meet LaTerral Williams</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("IT Support Specialist | Cloud Curious | Committed to Learning")
st.markdown("Welcome to my interactive portfolio. Built with [Streamlit](https://streamlit.io) and a lot of 🍕.")


