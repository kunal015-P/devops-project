pipeline {
    agent any

    environment {
        IMAGE_NAME = "kunal161/devops-app"
    }

    stages {
        stage("Checkout") {
            steps {
                git "https://github.com/kunal015-P/devops-project.git"
            }
        }

        stage("Build Image") {
            steps {
                sh "docker build -t $IMAGE_NAME:$BUILD_NUMBER ."
            }
        }

        stage("Push Image") {
            steps {
                withDockerRegistry([credentialsId: "dockerhub-creds"]) {
                    sh "docker push $IMAGE_NAME:$BUILD_NUMBER"
                }
            }
        }

        stage("Deploy to Kubernetes") {
            steps {
                sh "kubectl set image deployment/flask-app flask-app=$IMAGE_NAME:$BUILD_NUMBER"
            }
        }
    }
}
