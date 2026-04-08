pipeline {
    agent any
/*
    environment {
        AWS_REGION = 'ap-south-1'
        ECR_REPO = '<ECR_URI>'
    } */

    tools 		{
    	sonarRunner 'SonarScanner'
	}


    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/arpita497/mydevopsproject.git'
            }
        }

		stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=flask-app \
                    -Dsonar.sources=.
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: true
            }
       
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag flask-app:latest $ECR_REPO:latest'
            }
        }
/*
        stage('Push to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region $AWS_REGION \
                | docker login --username AWS --password-stdin $ECR_REPO

                docker push $ECR_REPO:latest
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        } */  
    }
}

