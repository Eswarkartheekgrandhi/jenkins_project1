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

                export BUILD_ID=dontKillMe

                nohup ./venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}