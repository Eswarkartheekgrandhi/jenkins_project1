pipeline {
    agent any

    environment {

        AWS_REGION = "us-east-1"

        REPOSITORY_URI = "682251233263.dkr.ecr.us-east-1.amazonaws.com/sum-app"

        IMAGE_NAME = "sum-app"

        IMAGE_TAG = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'ecr',
                    url: 'https://github.com/Eswarkartheekgrandhi/jenkins_project1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Login to Amazon ECR') {
            steps {
                sh """
                aws ecr get-login-password --region ${AWS_REGION} | \
                docker login --username AWS --password-stdin \
                ${REPOSITORY_URI.split('/')[0]}
                """
            }
        }

        stage('Tag Image') {
            steps {
                sh """
                docker tag ${IMAGE_NAME}:${IMAGE_TAG} \
                ${REPOSITORY_URI}:${IMAGE_TAG}
                """
            }
        }

        stage('Push Image') {
            steps {
                sh """
                docker push ${REPOSITORY_URI}:${IMAGE_TAG}
                """
            }
        }
    }

    post {

        success {
            echo "Docker Image Successfully Pushed to Amazon ECR 🚀"
        }

        failure {
            echo "Pipeline Failed ❌"
        }

    }
}