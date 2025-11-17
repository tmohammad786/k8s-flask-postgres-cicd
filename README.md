# flask-k8s-cicd

                   **  DevOps Kubernetes Assignment **

1.	Kubernetes Cluster Setup (Kops on AWS)
•	Created self-managed Kubernetes cluster using Kops.
•	S3 bucket for state store configured.
•	Cluster deployed with 1 master + 2 worker nodes.
•	Verified using kubectl get nodes.

2.	PostgreSQL StatefulSet
•	Deployed PostgreSQL 16 using StatefulSet.
•	Configured PVC with custom StorageClass.
•	Fixed mountpoint issue using PGDATA variable.
•	Verified using kubectl get pods -n database.

3.	Flask Application Deployment
•	Created sample Flask app.
•	Built Docker image and pushed to Docker Hub.
•	Deployment + Service created in Kubernetes.
•	ConfigMap + Secrets used for DB connection.

4.	NGINX Ingress Controller
•	Installed ingress-nginx via official manifests.
•	Created Ingress to expose Flask application.
•	Application accessible using AWS Load Balancer DNS

5.	Jenkins CI/CD Pipeline
•	Jenkins installed on EC2.
•	Pipeline stages: Checkout  Build  Push  Deploy.
•	kubeconfig added for cluster access.
•	Successful rollout of new image versions.

6.	Monitoring: Prometheus + Grafana
•	Installed Kube-Prometheus-stack via Helm.
•	Exposed Grafana via Ingress.
•	Imported dashboards for cluster/pod/node metrics.

7.	Final Deliverables
•	Working Kubernetes application.
•	Automated CI/CD.
•	Full monitoring and observability.
•	All components verified and screenshots captured.
 
•	

