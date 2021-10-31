pipeline {
  agent {
    kubernetes {
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    label: wog
spec:
  containers:
  - name: wog
    image: omryry/wog
"""
    }
  }
  stages {
    stage('run e2e') {
      steps {
        container('wog') {
          sh 'python /root/test_wog/test_e2e.py --driver /root/chromedriver'
        }
      }
    }
  }
}