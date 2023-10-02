# Plant Pathology App Deployment on AWS EKS

This README guides you through deploying a Flask-based Plant Pathology Application on AWS using Kubernetes (EKS).

## Prerequisites

1. **AWS CLI Setup**: Ensure the AWS CLI is installed and configured with the necessary IAM permissions.
2. **Install `kubectl`**: This is the Kubernetes command-line tool. [Installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
3. **Install `eksctl`**: A simple CLI tool for creating clusters on EKS. [Installation guide](https://eksctl.io/introduction/#installation).

## Steps

### 1. Dockerize the Flask App

Build the Docker image of your Flask app:
```bash
docker build -t plant-pathology-app .
```

Push the Docker image to AWS Elastic Container Registry (ECR) or any other container registry like Docker Hub.

### 2. Kubernetes Configuration

There are two main configuration files for deployment:

- `deployment.yaml`: Defines the application deployment on Kubernetes.
- `service.yaml`: Exposes the application using a service, in this case using a LoadBalancer which provisions an AWS ELB.

### 3. Deploy on Amazon EKS

a. **Create an EKS cluster**:
```bash
eksctl create cluster --name plant-pathology-cluster --version 1.21 --region us-west-1 --nodegroup-name standard-workers --node-type t2.medium --nodes 2
```

b. **Deploy the application**:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

c. **Check Deployment Status**:
```bash
kubectl get deployments
kubectl get services
```

The `EXTERNAL-IP` for the service is the address of the AWS ELB that routes traffic to your app.

### 4. Cleanup

Once you're done with testing, it's crucial to clean up resources to prevent unexpected AWS charges.

a. **Delete Kubernetes resources**:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

b. **Delete the EKS cluster**:
```bash
eksctl delete cluster --name plant-pathology-cluster
```

## Notes

This is a basic deployment guide. Depending on your requirements, consider further configurations (like database setup, secrets management, persistent storage, etc.). Always understand AWS pricing and be aware of provisioned resources to avoid unexpected charges.
