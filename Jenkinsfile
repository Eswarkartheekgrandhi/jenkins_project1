pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                if [ ! -d venv ]; then
                    python3 -m venv venv
                fi

                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f app.py || true

                BUILD_ID=dontKillMe nohup ./venv/bin/python app.py > app.log 2>&1 < /dev/null &
                '''
            }
        }
    }
}