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
                sh 'python3 --version'
                sh 'pytest --version'

            }
        }
    }
}