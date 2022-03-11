pipeline {
     agent
    {
        docker {
            //image 'safesecurity/pytest'
            image 'qnib/pytest'
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