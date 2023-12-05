pipeline {
  environment {
    PROJECT_FOLDER = 'ProjectB/microservices/products/'
  }
  agent {
    kubernetes {
      yaml """
apiVersion: v1
kind: Pod
metadata:
spec:
  # Use service account that can deploy to all namespaces
  serviceAccountName: jenkins-admin
  containers:
  - name: maven
    image: maven:3.3.9-jdk-8
    command:
    - cat
    tty: true
  - name: docker
    image: jenkins/inbound-agent
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
}
   }
   stages {
    stage('Clone') {
      steps {
          git branch: 'dev-test', changelog: false, poll: false, url: 'https://github.com/Smessages/ProjectB.git'
         }
      }
    }
    stage('build') {
      steps {
        container('docker') {
          script {
            def image = docker.build("jenkins/jnlp-slave","testing-image:$BUILD_NUMBER")
            image.inside(){
              sh "docker info"
            }
          }
        }
      }
    }
}
  

   
  

