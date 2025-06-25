pipeline{
	agent any
	stages{
		stage('checkout'){
			steps{
				git branch: 'main', url: 'https://github.com/sachink786/model-train-jen.git'
				}
			}
		stage('Install Dependencies'){
			steps{
				sh 'pip install -r requirements.txt --break-system-packages'
				}
			}
		stage('Train Model'){
			steps {
				sh 'python3 train.py'
				}
			}
		stage ('Test Model') {
			steps {
				sh 'python3 test.py'
				}
			}
 		stage('Archive Model') {
			steps {
				archiveArtifacts artifacts: 'model.pkl', fingerprint: true
				}
			}
		}
	}

