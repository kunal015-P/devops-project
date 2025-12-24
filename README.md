# devops-project
Project Explanation (Interview-Ready)

This project is a full DevOps deployment of a Flask application with a MySQL backend using Kubernetes on AWS.

I developed a Flask-based REST application that allows users to add data into a MySQL database using an HTTP endpoint. The application is containerized using Docker and served with Gunicorn for production readiness.

The container image is stored in Docker Hub, and the entire application is deployed on AWS EKS, which manages the Kubernetes cluster and worker nodes.

Inside Kubernetes:

The Flask application runs as a Deployment with multiple replicas for high availability.

MySQL runs as a separate pod and is exposed internally using a ClusterIP service.

A LoadBalancer service exposes the Flask application to the internet using an AWS Elastic Load Balancer.

Application configuration such as database host, username, and database name is managed using ConfigMaps.

Sensitive information like the database password is securely managed using Kubernetes Secrets.

The Flask application connects to MySQL using environment variables provided by Kubernetes, ensuring loose coupling between the application and infrastructure.

A Jenkins CI/CD pipeline automates the workflow:

It pulls the code from GitHub,

Builds a Docker image,

Pushes the image to Docker Hub,

Deploys the latest version to the Kubernetes cluster.

When a user accesses the application through the LoadBalancer URL, the request is routed to one of the Flask pods, which then inserts the data into the MySQL database and returns a success response.
