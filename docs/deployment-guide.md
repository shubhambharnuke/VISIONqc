# VisionQC Cloud Deployment Guide

This document provides exact steps to deploy the VisionQC platform to the cloud.

---

## 🚀 Option 1: 1-Click Multi-Service Deployment via Render (Free Tier)

A [`render.yaml`](../render.yaml) blueprint is configured in the repository root. It deploys both the FastAPI serving backend and Next.js frontend with automatic service discovery.

### Steps:
1. Go to [https://dashboard.render.com](https://dashboard.render.com) and sign in with your GitHub account (`shubhambharnuke`).
2. Click **New +** &rarr; **Blueprint**.
3. Select your repository: `shubhambharnuke/VISIONqc`.
4. Render will detect `render.yaml` and automatically configure:
   - `visionqc-backend` (FastAPI with model serving on Python 3.12).
   - `visionqc-frontend` (Next.js 16 with pre-configured API routing).
5. Click **Apply**.
6. Once deployed, Render will provide a public URL for your dashboard:
   `https://visionqc-frontend.onrender.com`

---

## 🚂 Option 2: Railway Full Stack (Instant Docker Deploy)

Railway provides native support for multi-container Docker applications.

### Steps:
1. Navigate to [https://railway.app](https://railway.app) and log in with GitHub.
2. Click **New Project** &rarr; **Deploy from GitHub repo**.
3. Choose `shubhambharnuke/VISIONqc`.
4. Add environment variables if prompted:
   - `APP_ENV`: `production`
   - `PORT`: `8000` (for backend) or `3000` (for frontend).
5. Railway provides automated SSL domains (`*.up.railway.app`).

---

## ⚡ Option 3: Instant Live Demonstration via Public Tunnel (Zero Setup)

If you need a live public URL right now for an evaluation, interview, or presentation without provisioning cloud infrastructure:

### Start the Local Servers:
```powershell
# Terminal 1 - Start Backend
python -m uvicorn backend.app.main:app --port 8000

# Terminal 2 - Start Frontend
cd frontend
npm run dev
```

### Expose to Public Internet via npx localtunnel:
```powershell
# Terminal 3 - Expose Frontend (Port 3000)
npx localtunnel --port 3000
```
This generates an immediate public HTTPS URL (e.g. `https://visionqc-demo.loca.lt`) that anyone on the internet can open to view and interact with your dashboard!

---

## 🐳 Option 4: Deploying on a Cloud VM (AWS EC2 / DigitalOcean / Lightsail)

If deploying to a single Ubuntu Cloud VM:
```bash
git clone https://github.com/shubhambharnuke/VISIONqc.git
cd VISIONqc
docker compose up -d --build
```
Everything (Postgres, Backend, Frontend, Prometheus, Grafana) will immediately run on the VM's public IP address.
