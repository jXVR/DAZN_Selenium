pipeline {
     agent
    {
        docker {
            image 'safesecurity/pytest'
        }
    }
    stages {
        stage('Build') {
            steps {
                script {
                sh 'java --version'
                sh 'python3 --version'
                sh 'python --version'
                sh 'pytest --version'
                }
            }
        }
    }
}