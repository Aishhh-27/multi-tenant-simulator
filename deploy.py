import os
import sys

def run(cmd):
    print(f"Running: {cmd}")
    os.system(cmd)

def create_namespace(ns):
    run(f"kubectl create namespace {ns}")

def deploy_app(ns):
    run(f"kubectl apply -f k8s/deployment.yaml -n {ns}")
    run(f"kubectl apply -f k8s/service.yaml -n {ns}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 deploy.py <tenant-name>")
        sys.exit(1)

    tenant = sys.argv[1]

    print(f"\n🚀 Deploying tenant: {tenant}")

    create_namespace(tenant)
    deploy_app(tenant)

    print(f"\n✅ Deployment completed for {tenant}")
    print(f"Check with: kubectl get all -n {tenant}")

if __name__ == "__main__":
    main()
