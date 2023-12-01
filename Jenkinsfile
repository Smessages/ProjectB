pipeline {
   agent any
   environment {
       registry = "arun33/"
       DOCKER_COMPOSE_FILE = 'microservices/docker-compose.yml'
   }
   stages {
       stage('Build') {
           agent {
               docker {
                   image 'arun33/test-jenag:1.0'
               }
           }
           steps {
               // Create our project directory.
               sh 'cd ${GOPATH}/src'
               sh 'mkdir -p ${GOPATH}/src/projectB'
               // Copy all files in our Jenkins workspace to our project directory.
               sh 'cp -r ${WORKSPACE}/* ${GOPATH}/src/projectB'
               // Build the app.
               sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} build'
           }
       }
   }
}

