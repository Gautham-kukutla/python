pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                bat'''rm -rf task
                git clone git@github.com:Gautham-kukutla/python.git task
                '''
            }
        }
        stage('Creating Files') {
            steps {
                bat '''cd task
                touch file.txt file1.txt file3.txt
                '''
            }
        }
        stage('Git Modification Check') {
            steps {
                bat'''pip install GitPython
                cd task
                pwd
                python python_script.py
                '''
            }
        }
    }
}
