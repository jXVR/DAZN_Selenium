pipeline {
     agent any
//     {
//         docker {
//             args '--privileged'
//             image 'qnib/pytest'
//         }
//     }
    stages {
        stage('Build') {
            steps {
                sh 'echo $SHELL'
                sh 'sw_vers'
                sh 'whoami'
                sh '/usr/local/bin/docker -v'
                sh 'docker -v'
            }
        }
    }
}