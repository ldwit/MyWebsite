import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="About Me", page_icon="🖥️", layout="wide")
apply_global_styles()
render_sidebar()

# Anchor for Back to Top
st.markdown('<a name="top"></a>', unsafe_allow_html=True)

# --- Header with Typewriter Effect ---
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
      margin: 0 auto 2rem auto;
      letter-spacing: .05em;
      animation: typing 3s steps(40, end), blink-caret .75s step-end infinite;
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

# --- About Me ---
st.markdown("### IT Support Specialist  |  Cloud Curious  |  Committed to Learning")

st.markdown("""
Passionate, curious, proactive IT professional with a comprehensive skill set in IT support. 
A proven track record in client support, proficient in utilizing existing documentation for issue resolution and complimentary customer service skills. 
Adept at conveying technical information, providing leadership, and contributing to a secure computing environment.
""")

st.markdown("---")

# --- Quick Info ---
st.markdown("""
- 🌍 Based in **Aubrey, TX**   
- ✉️ Contact: [laterral.williams@ldwit.com](mailto:laterral.williams@ldwit.com)  
- 🧠 Currently studying **Linux (RHEL 9)**
""")

st.markdown("---")


# View Resume as a Styled Button (opens in new tab)
st.markdown("### 📄 Resume")
st.markdown(
    """
    <style>
    .button-link {
        display: inline-block;
        padding: 0.5em 1.2em;
        font-size: 1rem;
        font-weight: 600;
        color: white;
        background-color: #0E1117;
        border: 2px solid #00FFF7;
        border-radius: 8px;
        text-decoration: none;
        transition: 0.3s ease;
    }
    .button-link:hover {
        background-color: #00FFF7;
        color: black;
        border: 2px solid #00FFF7;
    }
    </style>

    <a href="https://drive.google.com/file/d/1S4OgAwVbRElWEe4pmw3jmXfv7lBnCadk/view?usp=sharing" target="_blank" class="button-link">📂 View Resume</a>
    """,
    unsafe_allow_html=True
)

# --- Download Resume PDF ---
try:
    with open("assets/Resume_LWilliams.pdf", "rb") as file:
        st.download_button("📄 Download Resume", file, file_name="Resume_LWilliams.pdf")
except FileNotFoundError:
    st.error("Resume file not found. Please check the file path or deployment.")


st.markdown("---")

# --- Connect with Me ---
st.markdown("### 🌐 Connect with Me")
st.markdown("""
<p align="left">
  <a href="https://github.com/ldwit" target="_blank" rel="noreferrer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/ae/Github-desktop-logo-symbol.svg" width="32" height="32" alt="GitHub" />
  </a>
  <a href="https://www.linkedin.com/in/ldwit" target="_blank" rel="noreferrer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" width="32" height="32" alt="LinkedIn" />
  </a>
  <a href="https://dev.to/ldwit" target="_blank" rel="noreferrer">
    <img src="https://d2fltix0v2e0sb.cloudfront.net/dev-rainbow.svg" width="32" height="32" alt="Dev.to" />
  </a>
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Back to Top Button ---
st.markdown(
    """
    <a href="#top">
        <button style="position:fixed; bottom:40px; right:30px; background-color:#00FFF7;
                       color:black; border:none; border-radius:12px; padding:10px 16px;
                       font-weight:bold; cursor:pointer; box-shadow:0 4px 6px rgba(0,0,0,0.3);">
            ⬆️ Back to Top
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# --- Back Button ---
st.page_link("pages/Home.py", label="⬅️ Back to Home", icon="⬅️")