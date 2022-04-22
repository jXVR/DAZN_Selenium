pipeline {
    agent
    { dockerfile true }
    environment {
        DAZN_USER_DACH = credentials('DAZN_USER_DACH')
    }
    stages {
        stage('Build') {
            steps {
                script {
                sh "python3 ./assets/credentials_generator.py"
                sh 'python3 -m pytest ./pages_to_test/test_catalog_page.py'
                }
            }
        }
    }
}
