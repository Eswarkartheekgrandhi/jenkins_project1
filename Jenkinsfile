pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sh '''
                cd $WORKSPACE

                python3 -m venv venv
                . venv/bin/activate

                pip install flask

                pkill -f app.py || true

                nohup ./venv/bin/python app.py > app.log 2>&1 &
                disown
                '''
            }
        }
    }
}