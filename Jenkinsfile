pipeline {
    agent {
        docker {
            image 'qnib/pytest'
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