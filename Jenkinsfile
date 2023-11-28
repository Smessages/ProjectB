pipeline {
  agent any
  
  environment {
    PROJECT_DIR = '/home/jenkins'
    PROJECT_FOLDER = 'ProjectB'
    DOCKER_COMPOSE_FILE = 'microservices/docker-compose.yml'
  }

  stages {
    stage('Clone Git Repository') {
      steps {
        sh "git -C ${PROJECT_DIR} clone --recursive https://github.com/Smessages/ProjectB.git"
      }
    }

    stage('Build Microservices Images') {
      steps {
          sh "docker-compose -f ${DOCKER_COMPOSE_FILE} build"
      }
    }

    stage('Deploy Microservices Containers') {
      steps {
        input message: 'Approve deployment?', ok: 'Deploy'
        sh "docker-compose -f ${DOCKER_COMPOSE_FILE} down"
        sh "docker-compose -f ${DOCKER_COMPOSE_FILE} up -d"
        
      }
    }

    stage('Delete Unused Docker Images') {
      steps {
        sh 'docker system prune --all --force'
      }
    }
  }

  post {
    failure {
      echo "Build failed: ${currentBuild.result}"
    }
    success {
      echo "Build succeeded: ${currentBuild.result}"
    }
  }
}
