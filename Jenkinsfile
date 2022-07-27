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
    //NOTE if you run the below command port will be occupied by container until you dont stop jenkins or stop vm
    //so run only when needed.
    // docker run -d -p 5000:5000 hello_there command to rub container on port
    stage("run") {
      steps {
        sh """
          docker run -d hello_there
        """
      }
    }
  }
}