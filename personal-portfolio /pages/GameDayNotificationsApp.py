
import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Game Day Notifications App", page_icon="📣", layout="wide")

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
      color: #FFD700;
      overflow: hidden;
      border-right: .15em solid #FFD700;
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
      50% { border-color: #FFD700; }
    }
    </style>
    <div class="typewriter">
      <h2>📣 Initializing Project... ✅ Game Day Notifications App</h2>
    </div>
    """, unsafe_allow_html=True
)

# --- Project Overview ---
st.markdown("### 🏀 Project Overview")
st.write("""
A sports alert system delivering real-time NBA game day notifications via SMS or Email. Powered by AWS (SNS, Lambda, EventBridge) and external NBA APIs, it keeps fans updated with timely game information.
""")
st.markdown("---")

# --- Features ---
st.markdown("### ✨ Key Features")
st.markdown("""
- 📡 Fetches live NBA game scores via external API
- 📲 Sends updates to subscribers via SMS/Email using Amazon SNS
- 🕒 Automated delivery using EventBridge cron jobs
- 🔐 Security-first design with least privilege IAM roles
""")
st.markdown("---")

# --- Technologies Used ---
st.markdown("### 🧰 Tech Stack")
tech_cols = st.columns(4)
tech_stack = ["AWS SNS", "AWS Lambda", "Amazon EventBridge", "SportsData.io API"]
for i, tech in enumerate(tech_stack):
    with tech_cols[i]:
        st.markdown(f"🔹 {tech}")
st.markdown("---")

# --- GitHub and Resources ---
st.markdown("### 🔗 Resources")
st.markdown("[📂 GitHub Repository](https://github.com/ldwit/GameDayNotificationApp)")
st.markdown("[📺 Project Guidelines by REXTECH](https://www.youtube.com/watch?v=09WfkKc0x_Q)")
st.markdown("---")

# --- Project Structure ---
st.markdown("### 📁 Project Structure")
st.code("""
game-day-notifications/
├── src/
│   └── gd_notifications.py
├── policies/
│   ├── gd_sns_policy.json
│   ├── gd_eventbridge_policy.json
│   └── gd_lambda_policy.json
├── .gitignore
└── README.md
""")
st.markdown("---")

# --- Setup Instructions ---
st.markdown("### ⚙️ Setup Instructions")
st.markdown("#### 1. Clone or Recreate Project")
st.code("git clone https://github.com/ifeanyiro9/game-day-notifications.git")

st.markdown("#### 2. Create an SNS Topic")
st.markdown("Create a Standard SNS Topic and note the ARN.")

st.markdown("#### 3. Add Subscriptions")
st.markdown("Assign Email or SMS recipients via subscription options.")

st.markdown("#### 4. IAM Policies and Role")
st.markdown("Attach `gd_sns_policy`, `AWSLambdaBasicExecutionRole`, and assign to Lambda.")

st.markdown("#### 5. Deploy Lambda Function")
st.markdown("Use the code from `src/gd_notifications.py`, set environment variables: `NBA_API_KEY` and `SNS_TOPIC_ARN`.")

st.markdown("#### 6. Automate with EventBridge")
st.markdown("Use cron: `0 9-23/4 * * ? *` — triggers updates at 9AM, 1PM, 5PM, 9PM daily.")
st.markdown("---")

# --- Common Issues ---
st.markdown("### 🐞 Common Issues")
st.markdown("**1. Function Timeout**: Increase Lambda timeout to at least 10 seconds under Configuration settings.")
st.markdown("**2. EventBridge Cron**: Ensure expression matches intended run time:")
st.code("0 9-23/4 * * ? *")
st.markdown("---")

# --- Lessons Learned ---
st.markdown("### 🎓 Lessons Learned")
st.markdown("""
- Implementing SNS notifications via Lambda
- Automating triggers using EventBridge
- Writing fine-grained IAM policies for AWS services
- Handling API responses and sending dynamic alerts
""")
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

# --- Optional Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
