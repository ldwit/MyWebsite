
import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Tip Calculator App", page_icon="💸", layout="wide")

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
      <h2>💸 Initializing Project... ✅ Tip Calculator App</h2>
    </div>
    """, unsafe_allow_html=True
)

# --- Main Project Description ---
st.markdown("### 🧾 Project Overview")
st.write("""
The Tip Calculator App is a simple and interactive tool built with Python and Streamlit. It allows users to input a bill amount, choose a tip percentage, and split the total among multiple people.
""")
st.markdown("---")

# --- Optional GitHub Link ---
st.markdown("### 🔗 Project Repository")
st.markdown("[📂 View on GitHub](https://github.com/ldwit/TipCalculatorApp)")
st.markdown("---")

# --- Link to Web App ---
st.markdown("### 🚀 Launch the App")
st.markdown("[🌐 Open Tip Calculator App](https://tipcalculatorapp.streamlit.app/)")
st.markdown("---")

# --- Project Details ---
st.markdown("### 🔍 Project Details")
st.markdown("""
### 💡 Tip Calculator Web App

This interactive Python web app demonstrates:

- **Interactive UI Development**: A user-friendly interface created with Streamlit.
- **Web App Hosting**: Easily deployed on Streamlit Community Cloud.
- **Dynamic Input Handling**: Real-time bill, tip, and split calculations using Python.
- **Cloud-Ready Structure**: Clean file organization suitable for GitHub and deployment.

---

### 🌟 Key Features

- Customizable tip percentage slider  
- Bill splitting functionality  
- Real-time per-person cost calculation  
- Responsive and clean Streamlit interface  
- Rounded output to two decimal places  

---

### ⚙️ Technical Architecture

- **Language**: Python 3.x  
- **Framework**: Streamlit  
- **Deployment**: Streamlit Community Cloud  

---

### 📦 Core Dependencies

- `streamlit` – For building and serving the web app

---

### 📁 Project Structure

```
tip-calculator-streamlit/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

### 🛠️ Setup Instructions

**Step 1**: Clone the Repository

```
git clone https://github.com/ldwit/tip-calculator-streamlit.git
cd tip-calculator-streamlit
```

**Step 2**: (Optional) Create a Virtual Environment

```
python3 -m venv env
source env/bin/activate  # For Unix/Linux
```

**Step 3**: Install Dependencies

```
pip install -r requirements.txt
```

**Step 4**: Run the App Locally

```
streamlit run app.py
```

---

### 🐞 Common Issues

- **Streamlit Not Found**: Run `pip install streamlit`  
- **App File Not Detected**: Ensure `app.py` is in the correct location  
- **Outdated Python Version**: Use Python 3.7 or newer  

---

### 🎯 Learning Goals

- Python scripting for user input and calculations  
- Web app development with Streamlit  
- Hosting and deploying lightweight Python apps  
""")
st.markdown("---")

# --- Tools & Skills ---
st.markdown("### 🧰 Tools Used")
cols = st.columns(3)
tools = ["Python", "Streamlit", "GitHub"]
for i, tool in enumerate(tools):
    with cols[i]:
        st.markdown(f"🔹 {tool}")
st.markdown("---")

# --- Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
