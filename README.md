# 🚀 OptiScale Kube Platform
> **A High-Availability Microservices Architecture Orchestrated on Google Cloud GKE.**

![Build Status](https://img.shields.io/badge/Build-Passing-success?style=for-the-badge&logo=jenkins)
![Platform](https://img.shields.io/badge/Platform-GCP-blue?style=for-the-badge&logo=google-cloud)
![Infrastructure](https://img.shields.io/badge/Infra-Terraform-purple?style=for-the-badge&logo=terraform)
![Orchestration](https://img.shields.io/badge/K8s-GKE-326ce5?style=for-the-badge&logo=kubernetes)

## 📖 Overview
**OptiScale** is a fully automated DevOps platform designed to demonstrate self-healing infrastructure, zero-downtime deployments, and real-time observability. 

It deploys a stateful **Python/Flask** microservice backed by **Redis**, orchestrated by **Kubernetes (GKE)**, and monitored via a custom **Prometheus & Grafana** stack.

## 🏗️ Architecture
**CI/CD Pipeline Flow:**
`Developer` ➔ `GitHub` ➔ `Jenkins (CI)` ➔ `Docker Hub` ➔ `GKE Cluster (CD)`

**Microservices Architecture:**
* **Frontend:** Stateless Python Flask App (Auto-Scaling 1-10 Replicas).
* **Backend:** Redis Database (Persistent Storage).
* **Networking:** Google Cloud Load Balancer (Layer 7).
* **Observability:** Prometheus Scrapers & Grafana Dashboards.

## 🛠️ Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Cloud Provider** | Google Cloud Platform (GCP) | Hosting & Networking |
| **IaC** | Terraform | Provisioning GKE & VPCs |
| **Containerization** | Docker | Image building optimization |
| **Orchestration** | Kubernetes (GKE) | Pod management & Auto-healing |
| **CI/CD** | Jenkins | Automated Build & Deploy Pipelines |
| **Monitoring** | Prometheus + Grafana | Metrics visualization & Alerting |
| **Language** | Python (Flask) | Application Logic |

## 📊 Key Features
* ✅ **Self-Healing Infrastructure:** Automatically restarts crashed pods (demonstrated via Chaos Engineering).
* ✅ **Horizontal Pod Autoscaling:** Scales from 1 to 10 replicas based on CPU load.
* ✅ **Persistent Storage:** Data survives pod destruction using Redis Volume Claims.
* ✅ **Full-Stack Observability:** Custom Grafana dashboards tracking HTTP Request Rate & Latency.

## 📸 Screenshots

### 1. Mission Control Dashboard (Grafana)
*(Add your Screenshot of the Green Graph here)*
> Real-time traffic monitoring showing request spikes and microservice hits.

### 2. CI/CD Pipeline (Jenkins)
*(Add a Screenshot of your Jenkins Green Pipeline here)*
> Fully automated End-to-End deployment pipeline.

## 🚀 Getting Started

### Prerequisites
* Google Cloud Account
* Terraform installed
* Kubectl configured

### Deployment
1. **Provision Infrastructure**
   ```bash
   cd infrastructure
   terraform init
   terraform apply
   
2. **Deploy Microservices**
```bash
kubectl apply -f k8s-manifests/
```

3. **Access Application**

```bash

kubectl get service devops-app-service
# Open the EXTERNAL-IP in your browser
```

Built by Nadir | DevOps Engineer
   
   
