import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar


# --- Page Setup ---
st.set_page_config(page_title="Projects", page_icon="🧩", layout="wide")

# --- Anchor for Back to Top ---
st.markdown('<a name="top"></a>', unsafe_allow_html=True)

apply_global_styles()
render_sidebar()


# --- Typewriter Header with Embedded Navigation ---
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
      margin: 0 auto 1rem auto;
      letter-spacing: .05em;
      animation: typing 3s steps(40, end), blink-caret .75s step-end infinite;
    }

    .nav-links {
      display: flex;
      justify-content: left;
      gap: 30px;
      font-family: 'Segoe UI', sans-serif;
      font-size: 18px;
      margin-bottom: 2rem;
    }

    .nav-links a {
      color: #00FFF7;
      text-decoration: none;
    }

    .nav-links a:hover {
      text-decoration: underline;
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
      <h2>📂 Initializing Projects... ✅ All Projects</h2>
    </div>

    <div class="nav-links">
      <a href="#cloud-projects">☁️ Cloud Projects</a>
      <a href="#identity-projects">🛡️ Identity Projects</a>
      <a href="#python-projects">🐍 Python Projects</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Cloud Projects Section ---
st.markdown("### ☁️ <a id='cloud-projects'>Cloud Projects</a>", unsafe_allow_html=True)

st.markdown("#### 🔸 Game Day Schedule API")
st.write("A containerized sports API system using ECS Fargate, API Gateway, and Docker.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/GameDayScheduleAPI.py", label="🔗 View Project →", icon="📅")

st.markdown("#### 🔸 Game Day Notifications")
st.write("Real-time NBA score alerts via SNS using Lambda, EventBridge, and SportsData API.")  
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/GameDayNotificationsApp.py", label="🔗 View Project →", icon="🏀")

st.markdown("#### 🔸 Weather Dashboard")
st.write("Fetches real-time weather using OpenWeather API, stores data in S3, and runs Python logic for analysis.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/WeatherDashboardDemo.py", label="🔗 View Project →", icon="🌤️")

st.markdown("#### 🔸 Cloud Uploader CLI")
st.write("Bash-based tool to encrypt and upload files to GCP storage buckets.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/CloudUploaderCLI.py", label="🔗 View Project →", icon="☁️")
st.markdown("---")

# --- Identity Projects Section ---
st.markdown("### 🔐 <a id='identity-projects'>Identity Projects</a>", unsafe_allow_html=True)

st.markdown("#### 🔸 Okta + ServiceNow Integration")
st.write("Configured SAML SSO between Okta and ServiceNow for secure, seamless access.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/OktaAppIntegration_ServiceNow.py", label="🔗 View Project →", icon="🔐")

st.markdown("#### 🔸 GCP VM – AD Setup")
st.write("Provisioned a Windows Server VM on GCP and installed/configured Active Directory.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/GCPVM_AD.py", label="🔗 View Project →", icon="🖥️")

st.markdown("#### 🔸 AWS VM – AD Setup")
st.write("Deployed a Windows Server VM on AWS and configured Active Directory roles and DNS settings.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/AWSVM_AD_Okta.py", label="🔗 View Project →", icon="🧩")

st.markdown("#### 🔸 Okta + Salesforce SAML Integration")
st.write("Implemented SAML-based SSO between Okta and Salesforce with dynamic user provisioning.")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/SAML_Okta_Salesforce.py", label="🔗 View Project →", icon="🔐")
st.markdown("---")

# --- Python Projects Section ---
st.markdown("### 🐍 <a id='python-projects'>Python Projects</a>", unsafe_allow_html=True)

st.markdown("#### 🔸 Band Name Generator App  ")
st.markdown("Simple app that combines a city name and a pet’s name to create a band name.  ")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/BandNameGeneratorApp.py", label="🔗 View Project →", icon="🎶")

st.markdown("#### 🔸 Tip Calculator App  ")
st.markdown("Streamlit-based app that calculates tip amount and splits bill among people.  ")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/TipCalculatorApp.py", label="🔗 View Project →", icon="🧮")

st.markdown("#### 🔸 Warrior Wizard Dragon Game  ")
st.markdown("Interactive Streamlit game like Rock, Paper, Scissors.  ")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/WarriorWizardDragonApp.py", label="🔗 View Project →", icon="⚔️")

st.markdown("#### 🔸 Treasure Island Game  ")
st.markdown("Streamlit adventure game built as a beginner project.  ")
st.page_link("/workspaces/MyWebsite/personal-portfolio /pages/TreasureIslandApp.py", label="🔗 View Project →", icon="🗺️")
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