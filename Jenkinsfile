pipeline {
    agent { docker { image 'Python 3.8.10' } }
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