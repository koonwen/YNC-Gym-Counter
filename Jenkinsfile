pipeline {
    agent { docker { image 'python:3.9.6' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                echo 'Build requirements complete'
            }
        }
        stage('test') {
            steps {
                sh 'pytest -v'
                echo 'Testing complete'
            }
        }
    }
}