
import streamlit as st
import os
import time
from pathlib import Path

# --- Page Setup ---
st.set_page_config(page_title="👾 Digital Terminal", layout="centered")

# --- Add Matrix Background Effect ---
st.markdown("""
    <style>
        body {
            background-color: #000;
        }
        .matrix-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
            background: repeating-linear-gradient(
                to bottom,
                rgba(0, 255, 0, 0.1) 0px,
                rgba(0, 255, 0, 0.1) 2px,
                transparent 2px,
                transparent 4px
            );
            animation: move 0.3s linear infinite;
        }
        @keyframes move {
            0% {
                background-position: 0 0;
            }
            100% {
                background-position: 0 4px;
            }
        }
        .terminal-wrapper {
            position: relative;
            z-index: 1;
        }
    </style>
    <div class="matrix-background"></div>
""", unsafe_allow_html=True)


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

# --- Terminal Wrapper (to layer UI above animation) ---
st.markdown('<div class="terminal-wrapper">', unsafe_allow_html=True)


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
        <h3>ldwit@portfolio:~$</h3>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
```bash
📟 Initializing Personal Portfolio Shell...
Welcome to `LDWIT` portfolio site. Type the correct command below to enter:
ldwit@portfolio:~$ _
```
""")

# --- Command Entry ---
command = st.text_input("Enter command to continue:", label_visibility="collapsed")

if command.lower().strip() in ["init", "start", "launch", "sudo"]:
    with st.spinner("Loading environment..."):
        time.sleep(2)
    st.success("Access Granted ✅")
    st.page_link("pages/Home.py", label="➡️ Enter Site", icon="🔓")
elif command:
    st.error("Access Denied ❌ – Try: 'init', 'start', or 'launch'")

# --- Quote + Visitor Count ---
# st.markdown("<div class='quote'>\"Tell me and I forget, teach me and I may remember, involve me and I learn.\"<br>– Benjamin Franklin</div>", unsafe_allow_html=True)
st.markdown(f"<p style='color:#00ff00;'>👾 Visitor #: <strong>{count}</strong></p>", unsafe_allow_html=True)

# --- Optional Easter Egg ---
if command.lower().strip() == "sudo":
    st.balloons()
    st.markdown("💥 You found the easter egg! 🎉")

st.markdown('</div>', unsafe_allow_html=True)

