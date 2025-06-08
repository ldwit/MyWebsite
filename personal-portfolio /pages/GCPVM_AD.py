
import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="GCP VM – AD Setup", page_icon="🖥️", layout="wide")
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
      <h2>🖥️ Initializing Project... ✅ GCP VM – AD Setup</h2>
    </div>
    """, unsafe_allow_html=True
)

# --- Project Overview ---
st.markdown("### 📘 Project Overview")
st.write("""
This project involves setting up a virtual machine (VM) on Google Cloud Platform (GCP) and installing Active Directory (AD) on it.
The VM is configured with the e2-medium machine type and uses the Windows Server 2022 Datacenter boot image.
This guide provides step-by-step instructions for creating the VM, enabling necessary services, and configuring AD.
""")
st.markdown("---")

# --- Section: VM Creation ---
st.markdown("### ⚙️ Creating a Virtual Machine (VM) on GCP")
st.markdown("""
**Steps:**

1. Go to Google Cloud Console and select your project.
2. Navigate to `Compute Engine > VM instances` and click `Create instance`.
3. Configure:
   - **Name**: `your-vm-name`
   - **Region/Zone**: `us-central1` or your preferred region
   - **Machine type**: `e2-medium`
   - **Boot disk**: Windows Server 2022 Datacenter
   - **Firewall**: Allow HTTP and HTTPS traffic
   - **Networking**: Configure VPC/subnet/external IP as needed
4. Click `Create` and wait for provisioning.

**TLDR Configuration:**
- VM Name: `your-vm-name`
- Region/Zone: `us-central1`
- Machine Type: `e2-medium`
- Boot Disk: Windows Server 2022 Datacenter
""")
st.markdown("---")

# --- Section: AD Setup ---
st.markdown("### 🛠️ Installing and Configuring Active Directory")
st.markdown("""
**Steps:**

1. Use RDP to connect to the VM.
2. Set a strong local administrator password.
3. Open `Server Manager`, click `Manage > Add Roles and Features`.
4. Select the `AD DS` role and complete installation.
5. Promote the server to a Domain Controller using the Configuration Wizard:
   - Select `Add a new forest`
   - Set domain name and forest level
   - Define a DSRM password

6. (Optional) Configure DNS if prompted.

7. Post-install:
   - Open ports needed for AD
   - Apply Group Policies as needed

**TLDR Setup:**
- Domain Name: `your-domain-name`
- Forest Level: `forest-functional-level`
- DSRM Password: `your-dsrm-password`
""")
st.markdown("---")

# --- Section: Additional Considerations ---
st.markdown("### 📌 Additional Considerations")
st.markdown("""
- **Security**: Strong passwords, network firewall rules, disable RDP when not needed.
- **Backup**: Regularly snapshot the VM or backup AD data.
- **Monitoring**: Use Stackdriver or GCP Monitoring for uptime, logs, and performance.
""")
st.markdown("---")

# --- Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
