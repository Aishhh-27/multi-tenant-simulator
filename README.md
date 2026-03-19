# Multi-Tenant App Deployment Simulator

## Overview

This project simulates a **multi-tenant SaaS platform** on Kubernetes. Each tenant (customer) runs in its **own isolated namespace** with a separate Deployment and Service. The project demonstrates automation, Kubernetes resource management, and multi-tenant system design — skills highly relevant for SRE and platform engineering roles.

The deployment is automated via a Python script (`deploy.py`) that creates namespaces, deploys the app, and exposes it through a NodePort service.

---

## Features

- **Automated multi-tenant deployment**: Each tenant gets its own namespace, deployment, and service.
- **Python CLI**: Deploy tenants with a single command.
- **Kubernetes isolation**: Ensures tenant instances are independent.
- **Scalable**: Add as many tenants as needed without changing Kubernetes configurations.
- **Docker + Minikube**: Uses a local Kubernetes cluster for testing.

---

## Tech Stack

- **Kubernetes** – Namespaces, Deployments, Services  
- **Docker** – Containerized Python Flask app  
- **Python 3** – Automation script for deployments  
- **Minikube** – Local Kubernetes cluster  

---

### Prerequisites

- Docker installed
- Minikube installed and running
- Python 3.9+ installed

**Clone the repository**

git clone https://github.com/https://github.com/Aishhh-27/multi-tenant-simulator.git
cd multi-tenant-simulator

**Create and activate a Python virtual environment:**
python3 -m venv venv
source venv/bin/activate

**Start Minikube and configure Docker to point to Minikube’s environment**
minikube start --driver=docker
eval $(minikube docker-env)

**Build the tenant app Docker image inside Minikube:**
docker build -t tenant-app:v1 ./app

**Deploy a tenant by running:**
python deploy.py customer1

**This automatically creates a namespace, deployment, and service for the tenant. Access the tenant app in your browser using:**

minikube service tenant-service -n customer1 --url

**You can deploy additional tenants by running the same script with different tenant names:**
python deploy.py customer2
python deploy.py customer3

**Each tenant runs independently in its own namespace. To check pod status:**

kubectl get pods -n customer1
kubectl get pods -n customer2

**To delete a tenant and clean up all its resources:**

kubectl delete namespace customer1

**Project Structure**

multi-tenant-simulator/
│
├── app/
│   ├── app.py           # Flask app for tenant instances
│   └── Dockerfile       # Dockerfile to build tenant app image
│
├── k8s/
│   ├── deployment.yaml  # Kubernetes deployment template
│   └── service.yaml     # Kubernetes service template
│
├── deploy.py            # Python automation script
├── README.md
└── venv/                # Python virtual environment (ignored by git)

**Future Improvements**

Dynamic YAML generation per tenant

Additional CLI commands: create, delete, status

Resource limits and quotas per tenant

Ingress for centralized access

Monitoring and logging per tenant

**Key Takeaways**

Demonstrates multi-tenant SaaS simulation with Kubernetes

Shows automation and scripting skills using Python

Implements namespace isolation, mirroring real-world SRE platform requirements

Fully reproducible using Minikube + Docker locally

**Author**

**Aishwarya Ganesh**

```bash
git clone https://github.com/<your-username>/multi-tenant-simulator.git
cd multi-tenant-simulator
