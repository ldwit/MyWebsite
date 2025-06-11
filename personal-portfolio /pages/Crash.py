import streamlit as st
import time
import random

st.set_page_config(page_title="💥 Crash Detected", layout="centered")

# --- Hide Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- Inject Matrix Animation + Glitch Text Styling ---
st.markdown("""
<style>
html, body {
    height: 100%;
    margin: 0;
    overflow: hidden;
    background-color: black;
}

#matrixCanvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
}

.glitch-text {
    font-size: 1.8rem;
    color: #ff003c;
    text-shadow: 2px 2px #00ffea, -2px -2px #ff003c;
    animation: glitch 1s infinite;
    font-family: 'Fira Code', monospace;
    text-align: center;
    margin-top: 4rem;
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

<canvas id="matrixCanvas"></canvas>

<script>
const canvas = document.getElementById('matrixCanvas');
const ctx = canvas.getContext('2d');
canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

const cols = Math.floor(canvas.width / 20);
const ypos = Array(cols).fill(0);

function drawMatrix() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0f0';
    ctx.font = '16px monospace';

    ypos.forEach((y, i) => {
        const text = String.fromCharCode(33 + Math.random() * 94);
        ctx.fillText(text, i * 20, y);
        ypos[i] = y > 100 + Math.random() * 10000 ? 0 : y + 20;
    });
}

setInterval(drawMatrix, 50);
</script>
""", unsafe_allow_html=True)

# --- Random Joke Logic ---
jokes = [
    "Well, curiosity didn’t just kill the cat… it rebooted the portfolio.",
    "You had *one* job... and it wasn’t pressing the button.",
    "Big red button: 1 — Self-control: 0.",
    "Nice going. You’ve just launched the self-destruct sequence. Kidding… mostly.",
    "Welcome to the elite club of button-pressers. Population: you."
]

# --- Glitch Message & Joke ---
st.markdown("<h2 class='glitch-text'>!!! SYSTEM FAILURE: PORTFOLIO CORE BREACH !!!</h2>", unsafe_allow_html=True)
st.markdown("<h4 class='glitch-text'>Rebooting interface... hold tight.</h4>", unsafe_allow_html=True)
st.markdown(f"<h3 class='glitch-text'>🤖 {random.choice(jokes)}</h3>", unsafe_allow_html=True)

# --- Delay before redirect ---
time.sleep(5)
st.session_state.crash_mode = False
st.switch_page("Landing.py")
