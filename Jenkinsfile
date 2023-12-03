pipeline {
  environment {
    PROJECT_FOLDER = 'ProjectB/microservices/products/'
  }
  agent {
    kubernetes {
      cloud 'aroon-cluster'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: kubeagent
spec:
  # Use service account that can deploy to all namespaces
  serviceAccountName: jenkins-admin
  containers:
  - name: docker
    image: arun33/mybuilder:1.1
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
    - name: m2
      persistentVolumeClaim:
        claimName: m2
"""
}
   }
  stages {
    stage('clone git repo') {
      steps {
        sh """
           git clone https://github.com/Smessages/ProjectB.git
        """
      }
    }
    stage('build') {
      agent { dockerContainer 'jenkins/jnlp-slave:latest' }
      steps {
        sh """
          cd $PROJECT_FOLDER
          echo 'hello , docker'
          docker build -t aruun33/my-docker-image:$BUILD_NUMBER .
          """
        }
      }
    }
   
  }

