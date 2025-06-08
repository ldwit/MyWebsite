import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Okta App Integration", page_icon="🔐", layout="wide")

# --- Anchor for Back to Top ---
st.markdown('<a name="top"></a>', unsafe_allow_html=True)

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
      <h2>🔐 Initializing Project... ✅ Okta App Integration</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Project Description ---
st.markdown("### 🔧 Project Overview")
st.write("""
This project focuses on integrating **Okta** as an Identity Provider (IdP) with **ServiceNow** using Okta's App Integration Catalog/SAML Single Sign-On (SSO) for secure and seamless user authentication. It enables centralized access management and streamlined login experiences.
""")
st.markdown("---")

st.markdown("### 📋 Setup Instructions")

st.markdown("""
#### Step 1: Add ServiceNow to Okta
- Log in to the Okta Admin Console.
- Browse App Catalog > Search for **ServiceNow UD** > Click **Add Integration**.
- Configure instance name, placeholder info, and SAML settings:
  - **Single Sign-On URL**: `https://<instance_name>.service-now.com/navpage.do`
  - **Audience URI**: `https://<instance_name>.service-now.com`
- Configure attribute mappings and finish setup.
- Save and download the **IDP metadata** (XML).

#### Step 2: Configure ServiceNow
- Log into your ServiceNow instance.
- Install and activate: `Integration - Multiple Provider SSO (com.snc.integration.sso.multi)`
- Enable multi-provider SSO and create a **SAML 2.0 Identity Provider**.
- Import metadata from Okta.

#### Step 3: Assign Users in Okta
- Go to the Okta ServiceNow app > Assign > Select users/groups.
- Ensure user emails match between Okta and ServiceNow.

#### Step 4: Test SSO Connection
- Use the **Test Connection** button in ServiceNow.
- You should be redirected to Okta and logged in upon authentication.

#### Step 5: Launch from Okta Dashboard
- From the Okta dashboard, click the ServiceNow app to test seamless login.

---

### 🛠️ Troubleshooting Tips
- **Auto Redirect IDP**: Check under Related Links in ServiceNow.
- **Admin Role Issues**: Ensure your user has the **admin** role in the instance.
- **Email Mismatch**: Emails in Okta and ServiceNow must match.
- **Metadata URL**: Double-check the metadata file or URL in ServiceNow’s IdP config.

---

### 🎯 Key Learning Objectives
- Understand **SAML 2.0** and its use in SSO.
- Practice **Okta App Integration** and attribute mapping.
- Gain hands-on experience with **ServiceNow multi-provider SSO setup**.

---
""")

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

# --- Optional Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
