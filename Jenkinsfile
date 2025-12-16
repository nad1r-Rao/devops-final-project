pipeline {
    agent any

    environment {
        // Your Docker Hub Username
        DOCKERHUB_USERNAME = 'nadir468'
        
        // Name of the image we are building
        IMAGE_NAME = 'devops-final-project'
        
        // The secret ID we created in Jenkins
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Get the code from your GitHub
                git branch: 'main', url: 'https://github.com/nad1r-Rao/devops-final-project.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // Build the image and tag it with the Build Number (e.g., v1, v2, v3)
                    sh "docker build -t $DOCKERHUB_USERNAME/$IMAGE_NAME:$BUILD_NUMBER ."
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing to Docker Hub...'
                    // Login using the secret token (Password-Stdin is the secure way)
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    
                    // Push the tagged version
                    sh "docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:$BUILD_NUMBER"
                    
                    // Also push "latest" so Kubernetes can always find the newest one
                    sh "docker tag $DOCKERHUB_USERNAME/$IMAGE_NAME:$BUILD_NUMBER $DOCKERHUB_USERNAME/$IMAGE_NAME:latest"
                    sh "docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:latest"
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                // Remove the image from the Jenkins server to save space
                sh "docker rmi $DOCKERHUB_USERNAME/$IMAGE_NAME:$BUILD_NUMBER"
                sh "docker rmi $DOCKERHUB_USERNAME/$IMAGE_NAME:latest"
            }
        }
    }
}
