pipeline {
  agent {
    kubernetes {
      cloud 'aroon-cluster'
      label 'kubeagent'
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
      steps {
        container('docker') {
          sh """
             docker build -t arun33/my-docker-image:$BUILD_NUMBER -f ${WORKSPACE}/ProjectB/microservices/products/
          """
        }
      }
    }
    stage('Push') {
      steps {
        container('docker') {
          sh """
             docker push arun33/my-docker-image:$BUILD_NUMBER
          """
        }
      }
    }
  }
}
