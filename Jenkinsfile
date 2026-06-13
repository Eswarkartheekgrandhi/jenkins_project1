pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Eswarkartheekgrandhi/jenkins_project1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}