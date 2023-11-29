pipeline {
  agent any

  stages {
    stage('build') {
      steps {
        git url: 'https://github.com/tobydoescode/gh-gists.git', branch: 'main'
        sh 'docker build -t evoio/gh-gists:latest .'
      }
    }

    // stage('push') {

    // }

    // stage('deploy') {

    // }
  }
}
