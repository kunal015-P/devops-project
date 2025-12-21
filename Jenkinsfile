pipeline {
  agent any

  environment {
    IMAGE_NAME = "devops-app"
    DOCKERHUB_USER = "your_dockerhub_username"
  }

  stages {

    stage('Clone Repo') {
      steps {
        git 'https://github.com/yourname/devops-eks-project.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:latest .'
      }
    }

    stage('Push Image') {
      steps {
        withDockerRegistry([credentialsId: 'dockerhub-creds']) {
          sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
        }
      }
    }

    stage('Deploy to EKS') {
      steps {
        sh '''
          kubectl apply -f k8s/deployment.yaml
          kubectl apply -f k8s/service.yaml
        '''
      }
    }
  }
}
