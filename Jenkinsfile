pipeline {
  agent { label 'Production_Machine' }
  
  environment {
    PROJECT_DIR = '/home/jenkins/ProjectB'
    PROJECT_FOLDER = 'ProjectB'
    DOCKER_COMPOSE_FILE = 'microservices/docker-compose.yml'
    DOCKER_HUB_PAT = 'dckr_pat_BXrAyOA92onTtDGGiiG50vm0WaA'
    DOCKER_HUB_USER = 'arun33'
    
  }

  stages {
    stage('Clone Git Repository') {
      steps {
        sh "rm -rf ${PROJECT_DIR}"
        sh "mkdir -p ${PROJECT_DIR}"
        sh "git -C ${PROJECT_DIR} clone --recursive git@github.com:AbdelatifAitBara/ProjectB.git"
      }
    }

    stage('Build Microservices Images') {
      steps {
          sh "docker-compose -f ${DOCKER_COMPOSE_FILE} build"
      }
    }
    stage('Analyze image') {
            steps {
                // Install Docker Scout
                sh 'curl -sSfL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh | sh -s -- -b /usr/local/bin'
                
                // Log into Docker Hub
                sh 'echo $DOCKER_HUB_PAT | docker login -u $DOCKER_HUB_USER --password-stdin'

                // Analyze and fail on critical or high vulnerabilities
                sh 'docker-scout cves ${GIT_COMMIT} --exit-code --only-serverity critical,high'
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