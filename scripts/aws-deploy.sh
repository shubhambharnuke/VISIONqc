#!/bin/bash
# ==============================================================================
# VisionQC AWS EC2 / Lightsail User-Data Deployment Script
# Automatically provisions Docker, clones the repository, and starts all services
# ==============================================================================

set -e

echo "=== Updating packages and installing prerequisites ==="
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg git

echo "=== Installing Docker & Docker Compose Plugin ==="
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

echo "=== Cloning VisionQC Repository ==="
cd /home/ubuntu
if [ ! -d "VISIONqc" ]; then
  git clone https://github.com/shubhambharnuke/VISIONqc.git
fi

cd VISIONqc

echo "=== Launching VisionQC Full Stack with Docker Compose ==="
sudo docker compose up -d --build

echo "=== VisionQC Stack Deployment Complete ==="
sudo docker ps
