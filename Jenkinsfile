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
    image: maven:alpine
    command:
    - cat
    tty: true
  - name: docker
    image: docker:latest
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
        container('maven') {
          git branch: 'dev-test', changelog: false, poll: false, url: 'https://github.com/Smessages/ProjectB.git'
        }
      }
    }  
    stage('Build-Docker-Image') {
      steps {
        container('docker') {
          sh """
            cd $PROJECT_FOLDER
            docker build -t testing-image -f $PROJECT_FOLDER
          """
        }
      }
    }
    stage('Login-Into-Docker') {
      steps {
        container('docker') {
          sh 'docker login -u arun33 -p dckr_pat_bAaWdOnHOWD9HrjQyNXiKPhYrnc'
      }
    }
    }
    stage('Push-Images-Docker-to-DockerHub') {
      steps {
        container('docker') {
          sh 'docker push arun33/testing-image:$BUILD_NUMBER'
      }
    }
  }
  post {
    always {
      container('docker') {
        sh 'docker logout'
      }
      }
    }
  }
   
  }

