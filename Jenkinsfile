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
        stage('Run Backend') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker stop counter-backend || true && docker rm counter-backend || true"
                    // Run the backend container
                    docker.image('counter-backend').run('-d -p 5555:5555 --name counter-backend')
                }
            }
        }
        stage('Run Frontend') {
            steps {
                script {
                    // Stop and remove any existing container with the same name
                    sh "docker stop counter-frontend || true && docker rm counter-frontend || true"
                    // Run the frontend container
                    docker.image('counter-frontend').run('-d -p 80:80 --name counter-frontend')
                }
            }
        }
    }
}
