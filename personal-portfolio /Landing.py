
import streamlit as st
import os
import time
from pathlib import Path

# --- Page Setup ---
st.set_page_config(page_title="👾 Digital Terminal", layout="centered")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Visitor Counter File Path ---
counter_file = "assets/visit_counter.txt"
Path("assets").mkdir(parents=True, exist_ok=True)

# --- Visitor Count Logic ---
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    content = f.read().strip()
    count = int(content) + 1 if content else 1

with open(counter_file, "w") as f:
    f.write(str(count))

# --- Custom Styles ---
st.markdown("""
    <style>
        .terminal {
            background-color: #0d0d0d;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px #00ff00;
        }
        .terminal input {
            background-color: #000;
            color: #00ff00;
            border: none;
        }
        .quote {
            font-size: 1rem;
            color: #ccc;
            margin-top: 1rem;
            font-style: italic;
        }
        .loader {
            color: #00ff00;
            font-family: monospace;
            animation: blink 1s infinite;
        }
        @keyframes blink {
            50% { opacity: 0.0; }
        }
    </style>
""", unsafe_allow_html=True)

# --- Terminal Layout ---
st.markdown("""
    <div class="terminal">
        <h3>LaTerral@portfolio:~$</h3>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
### 👨‍💻 Digital Terminal Access Portal
Welcome to LaTerral Williams' interactive portfolio site. Type the correct command below to begin your journey:

```bash
LaTerral@portfolio:~$ _
```
""")

# --- Command Entry ---
command = st.text_input("Enter command to continue:", label_visibility="collapsed")

if command.lower().strip() in ["init", "start", "launch"]:
    with st.spinner("Loading environment..."):
        time.sleep(2)
    st.success("Access Granted ✅")
    st.page_link("pages/Home.py", label="💡 Enter Site", icon="🚀")
elif command:
    st.error("Access Denied ❌ – Try: 'init', 'start', or 'launch'")

# --- Quote + Visitor Count ---
st.markdown("<div class='quote'>\"Tell me and I forget, teach me and I may remember, involve me and I learn.\"<br>– Benjamin Franklin</div>", unsafe_allow_html=True)
st.markdown(f"<p style='color:#00ff00;'>👾 Visitor #: <strong>{count}</strong></p>", unsafe_allow_html=True)

# --- Optional Easter Egg ---
if command.lower().strip() == "sudo":
    st.balloons()
    st.markdown("💥 You found the easter egg! 🎉")
