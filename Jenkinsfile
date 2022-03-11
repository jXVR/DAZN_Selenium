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
                sh 'python --version'
                sh 'pytest --version'
                }
            }
        }
    }
}