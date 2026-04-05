pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/arpita497/mydevopsproject.git'
            }
        }

        stage('Build') {
            steps {
                echo "Build triggered by GitHub commit"
                sh '''
                  echo "Build RUN"
                  ls -la
                '''
            }
        }
    }

}
