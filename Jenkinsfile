pipeline {
  agent any

  stages {
    stage('Clone Git Repository') {
      steps {
        sh 'rm -rf /home/jenkins/ProjectB/'
        sh 'git -C /home/jenkins clone --recursive git@github.com:AbdelatifAitBara/ProjectB.git'
      }
    }

    
    stage('Scan Docker Images For Security Vulnerabilities') {
      steps {
        sysdigSecureScan(
          image: 'python:3.8-slim-buster',
          failBuildOnPolicyViolation: true,
          breakOnFail: true
        )
      }
    }

    stage('Build Microservices Images') {
      steps {
        // Build your microservices using Docker-compose
        sh 'docker-compose -f microservices/docker-compose.yml build'
      }
    }

    stage('Deploy Microservices Containers') { 
      steps {
        // Deploy your microservices using Docker-compose
        input message: 'Approve deployment?', ok: 'Deploy'
        sh 'docker-compose -f microservices/docker-compose.yml down'
        sh 'docker-compose -f microservices/docker-compose.yml up -d'
      }
    }

    stage('Delete Unused Docker Images') {
      steps {
        sh 'docker system prune --all --force'
      }
    }
  }
}