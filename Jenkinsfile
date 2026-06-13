pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sh '''
                python3 -m venv venv || true

                . venv/bin/activate

                pip install -r requirements.txt

                pkill -f app.py || true

                BUILD_ID=dontKillMe nohup ./venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}