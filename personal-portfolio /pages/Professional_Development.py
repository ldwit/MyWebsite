import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Professional Development", page_icon="🎓", layout="wide")
apply_global_styles()
render_sidebar()

# --- Header ---
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
      <h2>🧠 Initializing Learning... ✅ Professional Development</h2>
    </div>
    """, unsafe_allow_html=True
)

st.markdown("""
<blockquote style="font-size:18px;">“Education is the most powerful weapon which you can use to change the world.”<br>
<span style="float:center;">— Nelson Mandela</span></blockquote>
""", unsafe_allow_html=True)
st.markdown("---")

# --- Credly Profile ---
st.markdown("🔗 [My Credly Profile](https://www.credly.com/users/ldwit)")
st.markdown("---")

# --- Current Certifications ---
st.markdown("### 🏅 Current Certifications")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://images.credly.com/size/340x340/images/08096465-cbfc-4c3e-93e5-93c5aa61f23e/image.png",
        caption="Associate Cloud Engineer (Google Cloud)",
        width=115
    )

with col2:
    st.image(
        "https://images.credly.com/size/340x340/images/fc1352af-87fa-4947-ba54-398a0e63322e/security-compliance-and-identity-fundamentals-600x600.png",
        caption="Security, Compliance, & Identity Fundamentals",
        width=115
    )

with col3:
    st.image(
        "https://images.credly.com/size/340x340/images/2030e43f-8003-4d4b-9630-847add403c87/image.png",
        caption="Certified in Cybersecurity (ISC2)",
        width=115
    )

st.markdown("---")

# --- Current Studies ---
st.markdown("## 📘 Current Studies")
st.markdown("""
- **Red Hat Certified System Administrator (RHCSA)** — Currently studying through [CloudWhistler](https://www.cloudwhistler.com)
""")
st.markdown("---")

# --- Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")