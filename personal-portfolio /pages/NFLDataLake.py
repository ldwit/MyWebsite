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
      <h2>🖥️ Initializing Project... ✅ NFL Data Lake</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Project Description ---
st.markdown("### 📊 Project Overview")
st.write("""
The setup_nfl_data_lake.py script performs the following actions:

✅ Creates an Amazon S3 bucket to store raw and processed data.

✅ Uploads sample NFL player data (JSON format) to the S3 bucket.

✅ Creates an AWS Glue database and an external table for querying the data.

✅ Configures Amazon Athena for querying data stored in the S3 bucket.""")

# --- Architecture Diagram (Optional) ---
# st.image("assets/nfl_data_architecture.png", caption="System Architecture", use_column_width=True)

# --- Optional GitHub Link ---
st.markdown("### 🔗 Project Repository")
st.markdown("[📂 View on GitHub](https://github.com/ldwit/NFLDataLake)")

# --- Project Details ---
st.markdown("### 🔍 Project Details")
st.markdown("""
### 🏈 NFL Data Lake – AWS

This repository contains the `setup_nfl_data_lake.py` script, which automates the creation of a data lake for NFL analytics using AWS services. The script integrates **Amazon S3**, **AWS Glue**, and **Amazon Athena**, and sets up the infrastructure needed to store and query NFL-related data.

---

### 📁 Project Structure

```
NFLDataLake/
│
├── src/
│   ├── __init__.py
│   └── setup_nfl_data_lake.py
│
├── tests/           # Placeholder for test files
│
├── data/            # Placeholder for raw or processed data
│
├── requirements.txt
├── README.md
└── .env             # Environment variables for secure configurations
```

---

### ⚙️ Prerequisites

#### 1. AWS Account Setup

Create an AWS user with the following permissions:

- `AmazonS3FullAccess`  
- `AWSGlueServiceRole`  
- `AmazonAthenaFullAccess`  

Generate and securely store your **AWS access keys**.

#### 2. Environment Variables

Add the following keys to your `.env` file:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
SPORTS_DATA_API_KEY=your_sportsdata_api_key
NFL_ENDPOINT=https://api.sportsdata.io/v3/nfl/scores/json/Players
```

#### 3. Install Required Packages

Install dependencies using:

```
pip install -r requirements.txt
```

Make sure the following packages are listed in `requirements.txt`:

- `boto3`
- `requests`
- `python-dotenv`

---

### 🚀 Setup Instructions

#### Step 1: Configure AWS Resources

Run the Python script:

```
python3 src/setup_nfl_data_lake.py
```

The script will:

- Create the necessary S3 bucket  
- Fetch and upload NFL player data  
- Set up a Glue database and table  
- Configure Athena for querying the data

#### Step 2: Verify Resources

- **S3 Bucket**: Confirm it contains `raw-data/nfl_player_data.jsonl`
- **Glue Table**: Check for `nfl_players` table in AWS Glue Console
- **Athena Query**: Run a sample query like:

```
SELECT FirstName, LastName, Position, Team
FROM nfl_players
WHERE Position = 'QB';
```

---

### 🐞 Common Issues

#### 1. Invalid AWS Access Key Error

**Issue**:

```
An error occurred (InvalidAccessKeyId) when calling the CreateBucket operation
```

**Cause**:

- Incorrect or missing AWS credentials in `.env`
- Expired or revoked keys

**Solution**:

- Double-check `.env` for correct keys  
- Ensure your IAM user has appropriate permissions  
- If using EC2 or CloudShell, attach proper IAM role

---

#### 2. Invalid or Missing NFL Endpoint

**Issue**:

```
Invalid URL 'None': No scheme supplied.
```

**Cause**:

- Missing or incorrect `NFL_ENDPOINT` in `.env`

**Solution**:

- Set it correctly in `.env`:

```
NFL_ENDPOINT=https://api.sportsdata.io/v3/nfl/scores/json/Players
```

- Ensure your API key is valid and active

---

#### 3. Athena Query Result Location Not Configured

**Issue**:

```
Query failed: No query result location set for the query.
```

**Cause**:

- Athena result location not configured in the console

**Solution**:

- Go to **Athena Console** → **Settings**  
- Set result location to your S3 bucket, e.g.:

```
s3://your-bucket-name/athena-results/
```

- Confirm proper permissions are set on the bucket

---

### 📘 Key Learnings

- **AWS Services Integration**: Efficient use of S3, Glue, Athena  
- **Data Automation**: Automating infrastructure + ingestion  
- **Secure Configuration**: Managing credentials and tokens safely
""")

# --- Tools & Skills ---
st.markdown("### 🧰 Tools Used")
cols = st.columns(4)
tools = ["Python", "AWS S3", "Glue", "Athena"]
for i, tool in enumerate(tools):
    with cols[i]:
        st.markdown(f"🔹 {tool}")

# --- Optional Back Button ---
# st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
