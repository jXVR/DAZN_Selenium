pipeline {
     agent
    {
        any {
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