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
                sh """
echo 'USER_CREDENTIALS = [
    {
        "EMAIL": "$DAZN_USER_DACH_USR",
        "PASSWORD": "$DAZN_USER_DACH_PSW"
    },
]' > assets/user_data.py
                """
                sh 'python3 -m pytest ./pages_to_test/test_catalog_page.py'
                }
            }
        }
    }
}
