pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f app.py || true
                . venv/bin/activate
                nohup python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}