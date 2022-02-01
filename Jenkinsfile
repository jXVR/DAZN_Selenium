pipeline {
    agent none
    stages {
        stage('Back-end') {
            agent {
                docker { image 'qnib/pytest' }
            }
            steps {
                sh 'pytest -h'
            }
        }
    }
}