pipeline {
    agent {
        kubernetes {
            cloud 'aroon-cluster'
            defaultContainer 'jnlp'
            yaml """
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                app: aroon-cluster
            spec:
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
        stage('Build Docker Image') {
            steps {
                container('docker'){
                    sh 'hostname'
                    sh 'sleep 50'
                    sh 'docker --version'
                    sh 'git clone https://github.com/Smessages/ProjectB.git' 
                    sh 'docker build -t arun33/my-docker-image:1.0 -f ${WORKSPACE}/ProjectB/microservices/products/'
                } 
            }
        }
        stage('Push Docker Image') {
            steps {
                container('docker') {
                    sh 'docker push arun33/my-docker-image:1.0'
                }
            }
        }
    }
} 
