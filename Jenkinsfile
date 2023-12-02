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
              containers:
              - name: jnlp
                image: jenkinsci/jnlp-slave:alpine
                command: ["env"]
                tty: true
              volumes:
              - name: docker-sock
                hostPath:
                  path: /var/run/docker.sock
              - name: my-repo
                gitRepo:
                  repository: https://github.com/Smessages/ProjectB.git    
            """
        }
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'hostname'
                sh 'sleep 50'
                sh 'docker --version'
                sh 'git clone https://github.com/Smessages/ProjectB.git' 
                sh 'docker build -t arun33/my-docker-image:1.0 -f ${WORKSPACE}/ProjectB/microservices/products/'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push arun33/my-docker-image:1.0'
            }
        }
    }
}
 
