# Declarative Pipeline

## 문법
```
pipeline : 젠킨스의 파이프라인 코드라는것을 선언

agent : 파이프라인을 빌드 할 곳을 선택
- any : 추가적인 설정이 없다면 기본 설정된 master agent에서 실행된다.
- none : 설정안함 -> 따로 설정해주어야함

stages : 파이프라인의 작업의 단위인 stage를 위치시키는 블록, 반드시 하나 이상의 stage를 포함해야함

stage : 파이프라인의 작업(Check out, Test, Build, Deploy 등)의 단위 반드시 1개이상의 steps를 포함해야함

steps : stage에서 정의한 대로 작업을 정의하는 곳

echo : 메시지를 출력함 ex) echo 'hello world', echo "여기는 ${VALUE}입니다." -> ""을 사용해서 감싼다.

sh : shell script를 사용

writeFile : 파일을 생성

${VALUE} : 변수의 값을 사용

environment : 환경변수 설정 블럭

parameters : 변수 설정 블럭

post : 작업이 모두 끝나고 나서의 처리
```

## Jenkinsfile 작성
```
pipeline {
    agent none 
    options { skipDefaultCheckout(false)}
    stages {
        stage('git pull') {
            agent any 
            steps {
                checkout scm
            }
        }
        stage('Docker build') {
            agent any
            steps {
                sh 'docker build -t frontend:latest /var/jenkins_home/workspace/jenkins_test/frontend'
				sh 'docker build -t backend:latest /var/jenkins_home/workspace/jenkins_test/backend'
            }
        }
        stage('Docker run') {
            agent any
            steps {
                sh 'docker ps -f name=frontend -q \
        | xargs --no-run-if-empty docker container stop'
				sh 'docker ps -f name=backend -q \
		| xargs --no-run-if-empty docker container stop'

                sh 'docker container ls -a -f name=frontend -q \
        | xargs -r docker container rm'
				sh 'docker container ls -a -f name=backend -q \
		| xargs -r docker container rm'

                sh 'docker run -d --name backend \
                -p 8197:8197 \
                --network checkmate backend:latest'
                sh 'docker run -d --name frontend \
                -p 80:80 \
                -p 443:443 \
                -v /home/ubuntu/sslkey/:/var/jenkins_home/workspace/jenkins_test/sslkey/ \
                --network checkmate \
                frontend:latest'
            }
        }
    }
}
```