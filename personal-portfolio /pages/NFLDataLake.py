import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="NFL Data Lake", page_icon="🛰", layout="wide")

# Apply styles and sidebar
apply_global_styles()
render_sidebar()

# --- Header with Typewriter Animation ---
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
      <h2>🛰 Initializing Project: NFL Data Lake</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Project Description ---
st.markdown("## 📊 Project Overview")
st.write("""
This project leverages **Python, AWS Glue, S3, Athena**, and the **SportsData API** to build a cloud-based NFL data lake.

The goal is to create a scalable pipeline that collects, stores, and queries player stats for interactive analysis — all using serverless technologies.
""")

# --- Architecture Diagram (Optional) ---
# st.image("assets/nfl_data_architecture.png", caption="System Architecture", use_column_width=True)

# --- Key Features ---
st.markdown("## 🔍 Key Features")
st.markdown("""
- ✅ Real-time data ingestion from the SportsData.io API
- ✅ Storage in AWS S3 in raw and processed formats
- ✅ Table creation and queries via AWS Glue & Athena
- ✅ Python scripting with `boto3`, `requests`, and `.env` config
""")

# --- Tools & Skills ---
st.markdown("## 🧰 Tools Used")
cols = st.columns(4)
tools = ["Python", "AWS S3", "Glue", "Athena"]
for i, tool in enumerate(tools):
    with cols[i]:
        st.markdown(f"🔹 {tool}")

# --- Optional GitHub Link ---
st.markdown("## 🔗 Project Repository")
st.markdown("[📂 View on GitHub](https://github.com/ldwit/nfl-data-lake)")

# --- Optional Back Button ---
# st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
