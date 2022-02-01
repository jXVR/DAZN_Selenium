pipeline {
    agent
    {
        docker {
//             image 'qnib/pytest'
            label 'docker'
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