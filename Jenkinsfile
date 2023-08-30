pipeline {
  agent any

  stages {
    stage('Clone Git Repository') {
      steps {
        sh 'rm -rf /home/vagrant/agent/ProjectB/'
        sh 'git -C /home/vagrant/agent/ clone --recursive git@github.com:AbdelatifAitBara/ProjectB.git'
      }
    }

    stage('Remove The Old Containers and Images') {
      steps {
        script {
          sh 'docker rm -f product_container'
          sh 'docker rm -f order_container'
          sh 'docker rmi -f product_image'
          sh 'docker rmi -f order_image'
        }
      }
    }

    stage('Build Microservices Images') {
      steps {
        // Build your microservices using Docker-compose
        sh 'docker-compose -f microservices/docker-compose.yml build'
      }
    }
    
    stage('Deploy Microservices Containers') { 
      steps {
        // Deploy your microservices using Docker-compose
        sh 'docker-compose -f microservices/docker-compose.yml up -d'
      }
    }

/*    
    stage('Product Microservice Test') {
      steps {
        sh 'sleep 6'
        sh 'python3 -m unittest test_product.py'
      }
    }
*/    
  }
}