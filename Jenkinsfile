pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                // Checkout repository
                git 'https://github.com/Laiba-Noor/Mlops_Class_task_2_20i-1786'
            }
        }
        
        stage('Dependencies') {
            steps {
                // Install dependencies
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Testing') {
            steps {
                // Run tests
                sh 'pytest test.py'
            }
        }
        
        stage('Deployment') {
            steps {
                // Dummy deployment, you can customize this based on your actual deployment process
                script {
                    if (env.BRANCH_NAME == 'master') {
                        // Deploy to production
                        echo 'Deploying to production...'
                        // Add your deployment commands here
                    } else {
                        // Deploy to staging or any other environment
                        echo 'Deploying to staging...'
                        // Add your deployment commands here
                    }
                }
            }
        }
    }
}