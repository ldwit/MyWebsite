
import streamlit as st
from utils.style import apply_global_styles
from components.sidebar import render_sidebar

# --- Page Setup ---
st.set_page_config(page_title="Game Day Schedule API", page_icon="📅", layout="wide")

# --- Anchor for Back to Top ---
st.markdown('<a name="top"></a>', unsafe_allow_html=True)

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
      <h2>📅 Initializing Project... ✅ Game Day Schedule API</h2>
    </div>
    """, unsafe_allow_html=True
)

# --- Project Overview ---
st.markdown("### 📅 Project Overview")
st.markdown(""" 
This project demonstrates building a containerized API management system for querying sports data. It leverages Amazon ECS (Fargate) for running containers, Amazon API Gateway for exposing REST endpoints, and an external Sports API for real-time sports data. The project showcases advanced cloud computing practices, including API management, container orchestration, and secure AWS integrations.
""")

st.markdown("**GitHub Repo:** [GameDayScheduleAPI](https://github.com/ldwit/GameDayScheduleAPI)")
st.markdown("**Project Guidelines by REXTECH:** [Watch Here](https://www.youtube.com/watch?v=sF9_YzOrmTs&t=649s)")
st.markdown("---")

# --- Project Details ---
st.subheader("🏀 Project Details: Sports API Management System")
st.subheader("✨ Features")
st.markdown(""" 
- Exposes a REST API for querying real-time sports data  
- Runs a containerized backend using Amazon ECS with Fargate  
- Scalable and serverless architecture  
- API management and routing using Amazon API Gateway  
""")

st.subheader("🔧 Prerequisites")
st.markdown(""" 
- Sports API Key  
- AWS Account with basic ECS, API Gateway, Docker, and Python experience  
- AWS CLI installed and configured  
- Install Serpapi with: `pip install google-search-results`  
- Docker CLI and Desktop installed  
""")

st.subheader("🛠️ Technologies")
st.markdown(""" 
- **Cloud Provider:** AWS  
- **Core Services:** Amazon ECS (Fargate), API Gateway, CloudWatch  
- **Programming Language:** Python 3.x  
- **Containerization:** Docker  
- **IAM Security:** Custom least-privilege policies  
""")

st.subheader("📁 Project Structure")
st.code(""" 
sports-api-management/
├── app.py              # Flask application
├── Dockerfile          # Docker container setup
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md           # Documentation
""")
st.markdown("---")

# --- Setup Instructions ---
st.subheader("🚀 Setup Instructions")
st.markdown("""
1. **Clone the Repository**
```
git clone https://github.com/ifeanyiro9/containerized-sports-api.git  
cd containerized-sports-api  
```

2. **Create ECR Repository**
```
aws ecr create-repository --repository-name sports-api --region us-east-1  
```

3. **Authenticate, Build, and Push Docker Image**
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com  
docker build --platform linux/amd64 -t sports-api .  
docker tag sports-api:latest <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/sports-api:sports-api-latest  
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/sports-api:sports-api-latest  
```

4. **Set Up ECS Cluster with Fargate**  
- Create ECS Cluster and Task Definition  
- Configure Networking, Load Balancer, and Service  
- Test ALB and deploy

5. **Configure API Gateway**
- Create REST API  
- Setup HTTP Proxy integration to ALB  
- Deploy API and note the endpoint  

6. **Test API**
```
curl https://<api-gateway-id>.execute-api.us-east-1.amazonaws.com/prod/sports
```
""")
st.markdown("---")

# --- Learnings ---
st.subheader("📘 What We Learned")
st.markdown(""" 
- Setting up scalable, containerized applications with ECS  
- Creating public APIs using API Gateway  
""")
st.markdown("---")

# --- Enhancements ---
st.subheader("🔮 Future Enhancements")
st.markdown(""" 
- Add caching with Amazon ElastiCache  
- Integrate DynamoDB for personalized queries  
- Secure API Gateway with API Key or IAM auth  
- CI/CD automation for Docker deployments  
""")
st.markdown("---")

# --- Troubleshooting ---
st.subheader("🐞 Project Troubleshooting")
st.markdown("#### AWS ECR & ECS Troubleshooting Steps")
st.markdown("""
1. **Navigate to Amazon ECR Console**: https://console.aws.amazon.com/ecr/
2. **Verify Repository**: Confirm the repository `sports-api` exists.
3. **Check Image Tags**: Look for the `sports-api-latest` tag.
4. **Permission Issues**: Ensure necessary IAM permissions or contact your AWS administrator.
5. **Check Task Execution Role Permissions**:
   - Go to IAM Console: https://console.aws.amazon.com/iam/
   - Find the ECS task execution role
   - Attach the ECR permissions policy shown below
""")

st.code("""
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage"
      ],
      "Resource": "arn:aws:ecr:us-east-1:137068223119:repository/sports-api"
    }
  ]
}
""")

st.markdown("""
6. **Update Task Definition**: Create a new revision with the correct image URI.
7. **Update ECS Service**: Deploy with the new task definition.
8. **Monitor Tasks**: Use ECS console and CloudWatch logs to confirm new tasks start correctly.
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

# --- Back to Projects Button ---
st.page_link("pages/1_Projects.py", label="⬅️ Back to Projects", icon="⬅️")
