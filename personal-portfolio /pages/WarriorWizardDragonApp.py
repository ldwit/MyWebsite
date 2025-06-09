import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Warrior Wizard Dragon App", page_icon="🐉", layout="wide")

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
      <h2>🐉 Initializing Project... ✅ Warrior Wizard Dragon App</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Overview ---
st.markdown("### 📋 Project Overview")
st.write("""
A fun, Rock-Paper-Scissors-style game built with **Python** and **Streamlit**, where the **Wizard defeats the Dragon**, the **Warrior defeats the Wizard**, and the **Dragon defeats the Warrior**. Includes **ASCII art**, user vs computer gameplay, and an interactive UI.
""")
st.markdown("---")

# --- External Resources ---
st.markdown("### 🎥 Guided by Dr. Angela Yu")
st.markdown("[📘 Course Link](https://www.udemy.com/course/100-days-of-code/?kw=100+days+of+code&src=sac&couponCode=KEEPLEARNING)")
st.markdown("---")

# --- Live App + GitHub ---
st.markdown("### 🚀 Project Links")
st.markdown("[🌐 Launch Web App](https://wizardwarriordragonapp.streamlit.app/)")
st.markdown("[📂 View on GitHub](https://github.com/ldwit/WizardWarriorDragonApp)")
st.markdown("---")

# --- How to Play ---
st.markdown("### 🎮 How to Play")
st.markdown("""
- Launch the app locally or on Streamlit Cloud  
- Choose your champion: Warrior, Wizard, or Dragon  
- The computer randomly selects a challenger  
- Match outcomes follow these rules:
    - 🧙‍♂️ Wizard defeats 🐉 Dragon  
    - ⚔️ Warrior defeats 🧙‍♂️ Wizard  
    - 🐉 Dragon defeats ⚔️ Warrior  
- Results include fun ASCII art and clear win/loss messages  
""")
st.markdown("---")

# --- Tech Stack ---
st.markdown("### 🧰 Tech Stack")
cols = st.columns(2)
with cols[0]:
    st.markdown("🔹 Python 3.8+")
with cols[1]:
    st.markdown("🔹 Streamlit")

st.markdown("---")

# --- Installation Instructions ---
st.markdown("### 🛠️ Installation")
st.markdown("""
To run the project locally:

```
git clone https://github.com/ldwit/WizardWarriorDragonApp
cd warrior-wizard-dragon
```

**Create a virtual environment(optional):**

- macOS/Linux:
  ```
  python -m venv venv
  source venv/bin/activate
  ```

- Windows:
  ```
  python -m venv venv
  venv\\Scripts\\activate
  ```

**Install dependencies:**

```
pip install streamlit
```

**Run the app:**

```
streamlit run wizard_warrior_dragon.py
```
""")
st.markdown("---")

# --- Project Structure ---
st.markdown("### 📁 Project Structure")
st.code("""
warrior-wizard-dragon/
├── wizard_warrior_dragon.py   # Main Streamlit app
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
""")
st.markdown("---")

# --- Features ---
st.markdown("### 💡 Features")
st.markdown("""
- 🧙‍♂️ Mythical fantasy theme with ASCII art  
- ⚔️ User vs Computer battle  
- 🧠 Streamlit interface with interactive buttons  
- 🎯 Clear outcomes based on fantasy logic  
""")
st.markdown("---")

# --- Acknowledgements ---
st.markdown("### 🙌 Acknowledgements")
st.write("""
Built for fun, fantasy, and learning. Inspired by the simplicity of Rock-Paper-Scissors and the magic of text-based games.
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

# --- Back to Projects ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
