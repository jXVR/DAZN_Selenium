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
                sh 'python --version'
                sh 'pytest --version'

            }
        }
    }
}