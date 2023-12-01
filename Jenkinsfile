pipeline {
  agent any
  environment {
    registryCredential = 'dockerhub'
  }

  stages {
    stage('Clone Git Repository') {
      steps {
        sh "git clone --recursive https://github.com/Smessages/ProjectB.git"
      }
    }
    stage('Build Microservices Images') {
      steps {
          sh "cd ${WORKSPACE}/ProjectB/"
          sh "docker build -t arun33/products-k8s ."
      }
    }
    stage('Delete Unused Docker Images') {
      steps {
        sh 'rm -rf ${WORKSPACE}/ProjectB'
        sh 'docker system prune --all --force'
      }
    }
  }
}

