pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/<YOUR_GITHUB_USERNAME>/project1.git'
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