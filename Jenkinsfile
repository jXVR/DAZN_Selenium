pipeline {
    agent
    { dockerfile true }
    stages {
        stage('Build') {
            steps {
                script {
                sh 'python3 -m pytest ./pages_to_test/test_catalog_page.py'
                }
            }
        }
    }
}
