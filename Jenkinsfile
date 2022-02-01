pipeline {
    agent
    {
        docker {
            label 'docker'
            image 'qnib/pytest'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'sw_vers'
                sh 'whoami'
                sh '/usr/local/bin/docker -v'
                sh 'docker -v'
            }
        }
    }
}