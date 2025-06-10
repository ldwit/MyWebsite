import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Weather Dashboard Demo", page_icon="⛅", layout="wide")

# --- Anchor for Back to Top ---
st.markdown('<a name="top"></a>', unsafe_allow_html=True)

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
      <h2>⛅ Initializing Project... ✅ Weather Dashboard Demo</h2>
    </div>
    """, unsafe_allow_html=True
)

# --- Project Overview ---
st.markdown("### 📊 Project Overview")
st.write("""
This project is a Weather Data Collection System built using Python, AWS S3, and the OpenWeather API. 
It fetches, stores, and manages real-time weather data while showcasing core DevOps principles, Python development, and cloud integration skills.
""")
st.markdown("[📘 Project Guidelines by ShaeIntheCloud](https://www.youtube.com/watch?v=A95XBJFOqjw)")
st.markdown("---")

# --- Features ---
st.markdown("### 🌟 Key Features")
st.markdown("""
- **Real-Time Weather Data**: Fetches up-to-date weather information for multiple cities.  
- **Detailed Insights**: Displays temperature (°F), humidity, and conditions.  
- **Cloud Storage Integration**: Saves weather data to AWS S3.  
- **Bucket Name Randomization**: Appends unique tag to bucket names.  
- **Multi-City Monitoring**: Tracks weather in several cities.
""")
st.markdown("---")

# --- Technical Details ---
st.markdown("### 🛠️ Technical Architecture")
st.markdown("""
- **Language**: Python 3.x  
- **Cloud Provider**: AWS (S3)  
- **External API**: OpenWeather API  
""")
st.markdown("**Core Dependencies**")
st.code("boto3, python-dotenv, requests")
st.markdown("---")

# --- Project Structure ---
st.markdown("### 📁 Project Structure")
st.code("""
weather-dashboard/
├── src/
│   ├── __init__.py
│   └── weather_dashboard.py
├── tests/
├── data/
├── .env
├── .gitignore
├── requirements.txt
""")
st.markdown("---")

# --- Setup Instructions ---
st.markdown("### 🚀 Setup Instructions")
st.markdown("""
**Step 1**: Clone the repository  
```bash
git clone <repository-url>
cd weather-dashboard
```

**Step 2**: Create a virtual environment (optional)  
```bash
python3 -m venv env
source env/bin/activate
```

**Step 3**: Install dependencies  
```bash
pip install -r requirements.txt
```

**Step 4**: Configure environment variables  
Create a `.env` file with:  
```ini
OPENWEATHER_API_KEY=your_openweather_api_key
AWS_BUCKET_NAME_BASE=your_s3_bucket_name
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
```

**Step 5**: (Optional) Configure AWS CLI  
```bash
aws configure
```

**Step 6**: Run the app  
```bash
python src/weather_dashboard.py
```
""")
st.markdown("---")

# --- Common Issues ---
st.markdown("### 🐞 Common Issues")
st.markdown("""
- **Bucket Name Issues**: Ensure bucket names are unique and valid.  
- **AWS Credential Errors**: Verify correct setup with `aws configure`.  
- **API Key Errors**: Ensure valid OpenWeather API key.  
- **Missing Libraries**: Run `pip install -r requirements.txt`.  
- **Permission Denied**:  
```bash
chmod +x src/weather_dashboard.py
```

**CloudFormation Access Error** – Add this policy:
""")
st.code("""
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudformation:ListStacks",
      "Resource": "*"
    }
  ]
}
""", language="json")

# --- Learning Goals ---
st.markdown("### 🎯 Learning Goals")
st.markdown("""
- Python scripting and data processing  
- AWS S3 integration with Python  
- OpenWeather API consumption  
- Error handling and debugging in DevOps workflows  
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

# --- Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
