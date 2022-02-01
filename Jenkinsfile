pipeline {
    agent {
        docker {
            image 'qnib/pytest'
            args '--privileged'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -h'
            }
        }
    }
}