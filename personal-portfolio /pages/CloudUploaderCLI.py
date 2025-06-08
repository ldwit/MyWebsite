import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Cloud Uploader CLI", page_icon="☁️", layout="wide")
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
      <h2>☁️ Initializing Project... ✅ Cloud Uploader CLI</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Project Overview ---
st.markdown("### 📊 Project Overview")
st.write("""
The CLI Uploader Tool is a command-line utility for encrypting files and uploading them to Google Cloud Storage.
It supports file encryption, shareable link generation, file synchronization, and robust error handling.
""")
st.markdown("---")

# --- Project Links ---
st.markdown("### 🔗 Project Repository")
st.markdown("[📂 GitHub](https://github.com/ldwit/capstoneproject-clouduploadercli)")
st.markdown("---")

# --- Detailed Description ---
st.markdown("### 🔍 Project Details")
st.markdown("""
**Built from the Learn to Cloud Capstone Challenge**  
by Gwyneth Peña-Siguenza — [CloudCamp](https://www.madebygps.com/cloudcamp/)  

Inspired by: [Learn to Cloud Guide](https://learntocloud.guide/phase1/?ref=madebygps.com#capstone-project-clouduploader-cli)

---

### 🧠 Key Features

- **Usage Function**: Displays CLI usage instructions.
- **Google Cloud SDK Checks**: Verifies SDK installation and authentication.
- **Shareable Link Generation**: Adds public URLs when using `--share`.
- **File Synchronization**: Detects existing files; allows overwrite, skip, or rename.
- **File Encryption**: Optionally encrypt files using OpenSSL (`--encrypt`).
- **Bucket Management**: Confirms and creates storage buckets if needed.
- **Command-Line Flexibility**: Supports multiple files, storage classes, flags, and custom `gsutil` options.
- **Error Handling**: Clear success/failure messages per file; progress updates included.
- **Directory Support**: Uses `find` to traverse and upload all files in directories.

---

### 🛠️ Example Setup & Usage (Linux Terminal)

```bash
# Clone the repository
git clone https://github.com/ldwit/capstoneproject-clouduploadercli
cd capstoneproject-clouduploadercli

# View help menu
./upload.sh --help

# Upload with encryption and shareable link
./upload.sh --encrypt --share myphoto.jpg resume.pdf

# Upload entire directory
./upload.sh --encrypt --share ./mydocs
```

---

### 📁 Project Structure

```
capstoneproject-clouduploadercli/
├── upload.sh            # Main CLI script
├── README.md            # Project documentation
└── other_support_files  # Additional config or helper scripts (if applicable)
```

---

### 🎯 Learning Objectives

- Use of Bash scripting to automate cloud uploads.
- Managing encryption, error handling, and cloud integration.
- Leveraging GCP CLI tools effectively.
- Organizing a project for GitHub publishing.
""")
st.markdown("---")

# --- Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
