pipeline {

    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Eswarkartheekgrandhi/jenkins_project1.git'
            }
        }

        stage('Deploy Application') {
            steps {

                sh '''
                docker compose down || true

                docker compose up -d --build
                '''
            }
        }
    }

    post {

        success {
            echo 'Deployment Successful 🚀'
        }

        failure {
            echo 'Deployment Failed ❌'
        }
    }
}