# AWS Deployment Guide for VisionQC

This guide explains how to deploy the VisionQC platform to AWS.

---

## ⚡ Option 1: AWS EC2 / Lightsail (Recommended for Full Docker Stack)

Because VisionQC orchestrates 5 interconnected containers (PostgreSQL, FastAPI Backend, Next.js Frontend, Prometheus, and Grafana), running on a single Ubuntu instance via `docker-compose.yml` is the most cost-effective and straightforward AWS deployment.

### Specifications Recommended:
- **Instance Type:** `t3.medium` or `t3.large` (2 vCPU, 4–8 GB RAM)
- **OS:** Ubuntu 22.04 LTS or 24.04 LTS
- **Storage:** 20–30 GB gp3

---

### Step 1: Launch the EC2 Instance
1. Log in to the [AWS Management Console](https://console.aws.amazon.com/ec2).
2. Click **Launch Instance**:
   - **Name:** `visionqc-production`
   - **AMI:** Ubuntu Server 24.04 LTS (HVM)
   - **Instance Type:** `t3.medium` (or `t2.medium`)
   - **Key Pair:** Select your key pair or create one (e.g. `visionqc-key.pem`).

---

### Step 2: Configure Security Group (Firewall Rules)
Add inbound rules to allow access to the following ports:

| Type | Port Range | Source | Purpose |
|---|---|---|---|
| SSH | `22` | My IP | Secure Shell access |
| HTTP | `80` | `0.0.0.0/0` | Reverse proxy (optional) |
| Custom TCP | `3000` | `0.0.0.0/0` | **Next.js Frontend Dashboard** |
| Custom TCP | `8000` | `0.0.0.0/0` | **FastAPI Serving & Swagger Docs** |
| Custom TCP | `3001` | `0.0.0.0/0` | **Grafana Monitoring Dashboard** |
| Custom TCP | `9090` | `0.0.0.0/0` | **Prometheus Metrics** (optional) |

---

### Step 3: Run the Auto-Deployment Script
Under **Advanced details** &rarr; **User data**, paste the automated startup script:

```bash
#!/bin/bash
set -e
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg git

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl enable docker
sudo systemctl start docker

cd /home/ubuntu
git clone https://github.com/shubhambharnuke/VISIONqc.git
cd VISIONqc
sudo docker compose up -d --build
```

*(Alternatively, SSH into the machine: `ssh -i visionqc-key.pem ubuntu@<PUBLIC_IP>` and run `bash scripts/aws-deploy.sh`)*.

---

### Step 4: Access Your Live AWS Deployment
Once launched, find your **Public IPv4 Address** in the AWS console:
- **VisionQC Dashboard:** `http://<YOUR_AWS_PUBLIC_IP>:3000`
- **FastAPI Backend & API Docs:** `http://<YOUR_AWS_PUBLIC_IP>:8000/docs`
- **Grafana Monitoring:** `http://<YOUR_AWS_PUBLIC_IP>:3001` (`admin` / `admin`)
- **Prometheus Metrics:** `http://<YOUR_AWS_PUBLIC_IP>:9090`

---

## ☁️ Option 2: AWS App Runner / ECS Fargate (Serverless Containers)

If you prefer managed serverless containers instead of an EC2 instance:
1. Push `backend/Dockerfile` and `frontend/Dockerfile` to **Amazon ECR** (Elastic Container Registry).
2. Create two **AWS App Runner** services pointing to the respective ECR image URIs.
3. Set environment variable `NEXT_PUBLIC_API_URL` on the frontend service to point to the backend App Runner URL.
