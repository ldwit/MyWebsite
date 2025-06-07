import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Band Name Generator", page_icon="🎤", layout="wide")

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
      <h2>🎤 Initializing Project... ✅ Band Name Generator App</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Project Description ---
st.markdown("### 🎸 Project Overview")
st.write("""
The Band Name Generator is a simple, interactive Python app built as an introductory exercise in learning the language. It demonstrates:

- 🧑‍💻 User Interaction: Collecting input from users through prompts.
- ✂️ String Manipulation: Generating a custom band name using user-provided data.
- 🌐 Web App Deployment: Transforming a CLI-based script into an interactive web experience using Streamlit.
""")
st.markdown("---")

# --- External Resources ---
st.markdown("### 🎥 Guided by Dr. Angela Yu")
st.markdown("[📘 Course Link](https://www.udemy.com/course/100-days-of-code/?kw=100+days+of+code&src=sac&couponCode=KEEPLEARNING)")
st.markdown("---")

# --- GitHub & Launch Links ---
st.markdown("### 🔗 Project Links")
st.markdown("[📂 GitHub Repository](https://github.com/ldwit/BandNameGeneratorApp)")
st.markdown("[🚀 Launch the App](https://bandnamegeneratorapp.streamlit.app/)")
# st.markdown("[📘 Project Guidelines by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/?kw=100+days+of+code&src=sac&couponCode=KEEPLEARNING)")
st.markdown("---")

# --- Features ---
st.markdown("### 💡 Key Features")
st.markdown("""
- 📝 Interactive Input: Asks for the user’s hometown and pet’s name.
- 🔀 Dynamic Output: Generates a personalized band name by combining the two inputs.
""")
st.markdown("---")

# --- Technical Architecture ---
st.markdown("### 🧰 Tech Stack")
cols = st.columns(2)
tech_stack = ["Python 3.x", "Streamlit"]
for i, tech in enumerate(tech_stack):
    with cols[i]:
        st.markdown(f"🔹 {tech}")
st.markdown("---")

# --- Project Structure ---
st.markdown("### 📁 Project Structure")
st.code("""
band-name-generator/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
""")
st.markdown("---")

# --- Setup Instructions ---
st.markdown("### ⚙️ Setup Instructions")
st.markdown("""
**Step 1: Clone the Repository**

```
git clone https://github.com/ldwit/band-name-generator.git
cd band-name-generator
```

**Step 2: Install Dependencies**

```
pip install -r requirements.txt
```

**Step 3: Run the App Locally**

```
streamlit run app.py
```
""")
st.markdown("---")

# --- Common Issues ---
st.markdown("### 🐞 Common Issues")
st.markdown("""
- **Streamlit Not Installed**: Run `pip install streamlit`.
- **Script Won’t Run**: Ensure you are in the correct directory and that `app.py` exists.
- **Web App Doesn't Launch**: Check your browser; Streamlit usually opens a new tab automatically.
""")
st.markdown("---")

# --- Learning Goals ---
st.markdown("### 🎯 Learning Goals")
st.markdown("""
This project supports the following learning outcomes:

- 🧠 Basic Python Syntax: Practice with `input()` and `print()` functions.
- 🧺 Variable Handling: Store and combine user input.
- 🌍 Web Deployment Basics: Use Streamlit to turn a Python script into a browser app.
- 🗂 Version Control: Share and manage code via GitHub.
""")
st.markdown("---")

# --- Optional Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")