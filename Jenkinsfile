pipeline {
  agent any

  stages {
    stage('build') {
      steps {
        git url: 'https://github.com/tobydoescode/gh-gists.git', branch: 'main'
        sh 'docker build -t evoio/gh-gists:latest .'
      }
    }

    stage('push') {
      withCredentials([string(credentialsId: 'DOCKER_TOKEN', variable: 'TOKEN')]) {
        sh '''
          set +x
          docker login -u evoio -p $TOKEN
          docker push
        '''
      }
    }

    // stage('deploy') {

    // }
  }
}
