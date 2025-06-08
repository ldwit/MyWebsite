import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="AWS VM + AD + Okta Integration", page_icon="🛡️", layout="wide")

# Apply global styles and render sidebar
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
      <h2>🛠️ Initializing Project... ✅ AWS VM + AD + Okta</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Overview ---
st.markdown("### 🧭 Project Overview")
st.write("""
This project outlines the deployment of an Active Directory (AD) environment on an AWS Virtual Machine (VM) and the integration of Okta with AD using the Okta Active Directory Agent. 
You'll set up a Windows Server on AWS EC2, configure AD Domain Services, and link it to Okta for centralized identity management and SSO.
""")
st.markdown("---")

# --- AWS Setup Section ---
st.markdown("### ☁️ Setting Up Active Directory on an AWS Virtual Machine")
st.markdown("#### 🔐 Prerequisites")
st.write("""
- An active AWS account  
- Basic knowledge of AWS and Windows Server  
- RDP client for remote connection  
- AWS Key Pair for secure login  
""")

st.markdown("#### 🚀 Step-by-Step Setup")
st.markdown("##### Step 1: Set Up Your AWS Account")
st.write("Log in to the AWS Console and ensure proper permissions to create EC2 instances.")

st.markdown("##### Step 2: Launch an EC2 Instance")
st.write("""
- AMI: Windows Server 2022 Base (used here)  
- Instance Type: t2.micro (Free tier eligible)  
- Key Pair: Create or use an existing one  
- Network Settings: Use a VPC with public IP  
- Storage: Minimum 50GB recommended  
""")

st.markdown("##### Step 3: Configure Security Group")
st.write("""
Allow these ports:
- RDP (3389), DNS (53), LDAP (389), SMB (445), Global Catalog (3268), Time Sync (123)
""")

st.markdown("##### Step 4: Connect to the EC2 Instance")
st.write("Use RDP and admin credentials from the EC2 Console to access your instance.")

st.markdown("##### Step 5: Install Active Directory")
st.write("""
- Use Server Manager to add AD DS role  
- Promote server to a domain controller  
- Create a new forest and domain (e.g., `example.com`)  
""")

st.markdown("##### Step 6: Optional DNS Configuration")
st.write("Use built-in AD DNS or integrate with Route 53 if needed.")

st.markdown("##### Step 7: Test the AD Environment")
st.write("Verify using ADUC (Users and Computers), create test users and OUs.")
st.markdown("---")

# --- Okta Agent Setup ---
st.markdown("### 🔗 Installing and Setting Up the Okta Active Directory Agent")
st.markdown("#### 🔐 Prerequisites")
st.write("""
- Okta Admin Account  
- AD environment running on Windows Server  
- AD credentials and OU/Group structure preconfigured  
""")

st.markdown("#### 🛠️ Setup Steps")
st.markdown("##### Step 1: Prepare Okta")
st.write("Log into Okta Admin → Directory → Directory Integrations → Add AD")

st.markdown("##### Step 2: Download and Install AD Agent")
st.write("Transfer and run the Okta AD Agent installer on your AD server.")

st.markdown("##### Step 3: Install & Configure")
st.write("""
- Enter Okta Org URL and Activation Token  
- Use server admin credentials  
- Complete install and verify connection in Okta  
""")

st.markdown("##### Step 4: Directory Integration in Okta")
st.write("""
- Select OUs to sync  
- Set import/sync frequency  
- Optional: Enable Password Sync  
""")

st.markdown("##### Step 5: Verify Integration")
st.write("""
- Manually trigger sync from Okta  
- Test user login via Okta with AD credentials  
- Confirm proper group/user mapping  
""")
st.markdown("---")

# --- Security and Maintenance ---
st.markdown("### 🔒 Secure and Optimize")
st.write("""
- Install the Okta agent on multiple servers for high availability  
- Allow outbound TCP port 443 for agent connectivity  
- Monitor in Okta Admin under Directory Integrations  
- Adjust attribute mappings in Profile Editor  
""")
st.markdown("---")

# --- Learning Outcomes ---
st.markdown("### 📘 Key Learning Objectives")
st.write("""
- Understand SAML-based identity integration  
- Set up AD on AWS EC2  
- Install and manage Okta AD Agent  
- Configure secure user and group sync  
- Perform basic SSO and AD testing  
""")
st.markdown("---")

# --- Optional Back Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")