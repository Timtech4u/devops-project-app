pipeline {
    agent any

    stages {
        stage('Build Backend') {
            steps {
                script {
                    docker.build('counter-backend', 'backend')
                }
            }
        }
        stage('Build Frontend') {
            steps {
                script {
                    docker.build('counter-frontend', 'frontend')
                }
            }
        }
    }
}
