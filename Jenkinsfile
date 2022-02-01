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
                sh 'docker -v'
            }
        }
    }
}