import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="SAML Integration – Okta & Salesforce", page_icon="🔐", layout="wide")

# Apply global styling and sidebar
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
      <h2>🔐 Initializing Project... ✅ SAML Integration</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Project Overview ---
st.markdown("### 📋 Project Overview")
st.write("""
This project provides step-by-step instructions for setting up a **SAML integration** between **Okta** and **Salesforce** to enable Single Sign-On (SSO).
""")
st.markdown("---")

# --- External Resource ---
st.markdown("### 🎥 Integration Walkthrough by AskmeIdentity")
st.markdown("[📺 Watch on YouTube](https://www.youtube.com/watch?v=75bFlR5SELo&list=PLLtgG_DQlifXL2TYeYpzn-AnF5yEJ1OQQ&index=14)")
st.markdown("---")

# --- Prerequisites ---
st.markdown("### ⚙️ Prerequisites")
st.markdown("""
- ✅ **Okta Admin (Dev) Account** with access to the Admin Console  
- ✅ **Salesforce Admin (Dev) Account** with administrator privileges
""")
st.markdown("---")

# --- Step-by-Step Setup ---
st.markdown("### 🛠️ Step-by-Step Instructions")

st.markdown("#### 1. Set Up Okta Application for Salesforce")
st.markdown("""
- Navigate to **Applications > Applications** → Create App Integration  
- Select **SAML 2.0**, click **Next**  
- Fill in a temporary SAML config (you’ll update this later)  
- Save IDP metadata (XML format)  
""")

st.markdown("#### 2. Configure SAML Settings in Salesforce")
st.markdown("""
- Go to **Setup** → Search **Single Sign-On Settings**  
- Enable SSO and **create a new SAML config** using Okta metadata  
- Upload certificate, enter Issuer & ACS URL  
- Download Salesforce metadata and update values in Okta  
- Enable SAML and authentication domain  
""")

st.markdown("#### 3. Assign Users")
st.markdown("""
- In Okta: Go to the Salesforce app → Assign Users/Groups  
- In Salesforce: Ensure user info matches Okta, activate account  
""")

st.markdown("#### 4. Test the Integration")
st.markdown("""
- Log in via Okta using the Audience/Entity ID URL  
- If mapped correctly, you’ll be redirected into Salesforce  
""")
st.markdown("---")

# --- Troubleshooting Tips ---
st.markdown("### 🐞 Troubleshooting Tips")
st.markdown("""
- **User Profile Mismatch**: Check user identifiers in Okta vs. Salesforce  
- **Certificate Errors**: Ensure correct metadata and certificate were uploaded  
""")
st.markdown("---")

# --- Key Learnings ---
st.markdown("### 📘 Key Learning Objective")
st.write("""
By completing this setup, you've enabled **secure SSO integration** between Okta and Salesforce using **SAML 2.0**, enhancing identity federation and user experience.
""")
st.markdown("---")

# --- Tools & Skills ---
st.markdown("### 🧰 Tech Stack")
cols = st.columns(3)
tools = ["Okta", "Salesforce", "SAML 2.0"]
for i, tool in enumerate(tools):
    with cols[i]:
        st.markdown(f"🔹 {tool}")
st.markdown("---")

# --- Optional Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
