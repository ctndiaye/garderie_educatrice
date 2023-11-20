pipeline {
  agent {
    label 'python_docker_slave'
  }
  stages{
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }
    }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Tests unitaires') {
      steps {
        sh 'python manage.py test'
      }
    }
  }
}