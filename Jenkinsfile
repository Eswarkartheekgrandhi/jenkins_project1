pipeline {
    agent any

    environment {
        IMAGE_NAME = "sum-app"
        CONTAINER_NAME = "sum-app-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Eswarkartheekgrandhi/jenkins_project1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop Old Container') {
            steps {
                sh """
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                """
            }
        }

        stage('Run New Container') {
            steps {
                sh """
                docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
                """
            }
        }
    }

    post {
        success {
            echo "Deployment Successful 🚀"
        }
        failure {
            echo "Deployment Failed ❌"
        }
    }
}