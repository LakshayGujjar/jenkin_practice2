pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t hello_there .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run -d -p 5000:5000 --name hello_there
        """
      }
    }
  }
}