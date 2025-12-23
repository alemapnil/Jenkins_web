// 以下是在名為192.168.1.83 的node上，建置pipeline的Jenkinsfile
pipeline{
    agent {
        label '192.168.1.83'
    }
    stages{
        stage('init'){
            steps{
                echo "此為Git上的Jenkinsfile"
                git branch: 'main', credentialsId: '7c359d4c-fd1b-49df-97df-7867f3e19e0f', url: 'https://github.com/alemapnil/Jenkins_web.git'
                sh 'pwd'
            }
        }
        stage('virtual'){
            steps{
                sh '''
                sudo apt update
                sudo apt install -y \
                    python3 \
                    python3-pip \
                    python3-venv
                '''

                echo "Python 安裝完畢"
                sh 'python3 -m venv myenv'
                echo "啟動虛擬環境"
                sh 'source myenv/bin/activate'
            }
        }
        
        stage('check'){
            steps{
                echo "檢查環境安裝"
                sh "python --version"
                sh "django-admin --version"
            }
        }
        stage('install'){
            steps{
                echo "要安裝了"
                sh "python -m pip install Django"
            }
        }
        stage('running'){
            steps{
                echo "要跑了..."
                sh "python manage.py runserver"
                
            }
        }
    }
    post{
        always{
            echo"總是執行"
        }
        success{
            echo"成功才執行"
                mail to: 'pamela.lin@nadisystem.com',
                subject: "[Pipeline] ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
                body: "請查看 Jenkins Console: ${env.BUILD_URL}"
        }
        failure{
            echo"失敗才執行"
                mail to: 'pamela.lin@nadisystem.com',
                subject: "[Pipeline] ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
                body: "請查看 Jenkins Console: ${env.BUILD_URL}"
        }
        unstable{
            echo"不穩定才執行"
        }
        changed{
            echo"狀態改變才執行，例如先前失敗或成功，反之亦然"
        }
    }
}