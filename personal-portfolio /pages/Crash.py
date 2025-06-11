
import streamlit as st
import time
import random

st.set_page_config(page_title="💥 Crash Detected", layout="wide")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            display: none;
        }
        html, body {
            height: 100%;
            margin: 0;
            overflow: hidden;
            background-color: #001f00;
        }
        .background {
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            z-index: -1;
        }
        .glitch-text {
            font-size: 2rem;
            color: #ff003c;
            font-family: 'Fira Code', monospace;
            text-align: center;
            margin-top: 6rem;
            text-shadow: 2px 2px #00ffea, -2px -2px #ff003c;
            animation: glitch 1s infinite;
        }
        @keyframes glitch {
            0% { transform: translate(0); }
            20% { transform: translate(-1px, 1px); }
            40% { transform: translate(2px, -2px); }
            60% { transform: translate(-2px, 2px); }
            80% { transform: translate(1px, -1px); }
            100% { transform: translate(0); }
        }
    </style>
    <div class="background">
        <canvas id="matrix"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');
        canvas.height = window.innerHeight;
        canvas.width = window.innerWidth;
        const cols = Math.floor(canvas.width / 20);
        const ypos = Array(cols).fill(0);
        function matrix() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "#0F0";
            ctx.font = "16pt monospace";
            ypos.forEach((y, ind) => {
                const text = String.fromCharCode(33 + Math.random() * 94);
                const x = ind * 20;
                ctx.fillText(text, x, y);
                if (y > 100 + Math.random() * 10000) ypos[ind] = 0;
                else ypos[ind] = y + 20;
            });
        }
        setInterval(matrix, 50);
    </script>
""", unsafe_allow_html=True)

# --- Joke logic ---
jokes = [
    "Well, curiosity didn’t just kill the cat… it rebooted the portfolio.",
    "You had *one* job... and it wasn’t pressing the button.",
    "Big red button: 1 — Self-control: 0.",
    "Nice going. You’ve just launched the self-destruct sequence. Kidding… mostly.",
    "Welcome to the elite club of button-pressers. Population: you."
]
joke = random.choice(jokes)

# --- Display messages ---
st.markdown("<h2 class='glitch-text'>!!! SYSTEM FAILURE: PORTFOLIO CORE BREACH !!!</h2>", unsafe_allow_html=True)
st.markdown("<h4 class='glitch-text'>Rebooting interface... hold tight.</h4>", unsafe_allow_html=True)
st.markdown(f"<h3 class='glitch-text'>🤖 {joke}</h3>", unsafe_allow_html=True)

# --- Redirect after delay ---
time.sleep(5)
st.session_state.crash_mode = False
st.switch_page("Landing.py")
