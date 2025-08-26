pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'envSetup', url: 'https://github.com/JITHINPDEV/pytest.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest Tests/ --html=report.html --self-contained-html -v'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'UI Test Report'
                ])
            }
        }
    }
}
