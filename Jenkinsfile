pipeline {
    agent any
//    {
//        docker {
//            image 'qnib/pytest'
  //          args '--privileged'
   //     }
    //}
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