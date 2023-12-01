pipeline {
   agent any
   environment {
       registry = "arun33/"
       DOCKER_COMPOSE_FILE = 'microservices/docker-compose.yml'
       APPCACHE = "/tmp"
   }
   stages {
       stage('Build') {
           agent {
               any {
                   image 'arun33/test-jenag:1.0'
               }
           }
           steps {
               // Create our project directory.
               sh 'cd ${APPCACHE}/'
               sh 'mkdir -p ${APPCACHE}/projectB'
               // Copy all files in our Jenkins workspace to our project directory.
               sh 'cp -r ${WORKSPACE}/* ${APPCACHE}/projectB'
               // Build the app.
               sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} build'
           }
       }
   }
}

