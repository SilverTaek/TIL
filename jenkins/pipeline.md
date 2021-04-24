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
pipeline { //파이프라인이라는것을 선언
    agent none // none이기때문에 master agent에서 실행
    options { skipDefaultCheckout(false)}
    stages {
        stage('git pull') { # pull 받아오는 상태
            agent any //마스터에서 실행
            steps {
                checkout scm
            }
        }
        stage('Docker build') { #docker build 상태
            agent any
            steps {
                sh 'docker build -t frontend:latest /var/jenkins_home/workspace/jenkins-cicd/frontend' 
				# frontend -t 는 생성할 이미지 이름. 
				sh 'docker build -t backend:latest /var/jenkins_home/workspace/jenkins-cicd/backend' 
				# backend 도커가 있는 위치. 빌드는 도커 이미지 파일을 만들어 주는 것입니다!! 아직 실행 X
            }
        }
        stage('Docker run') { # docker 배포 상태
            agent any
            steps {
                # 도커 시작 전, 기존에 실행중인 도커를 멈추고 제거하는 작업
                sh 'docker ps -f name=frontend -q \
        | xargs --no-run-if-empty docker container stop'
				sh 'docker ps -f name=backend -q \
		| xargs --no-run-if-empty docker container stop'

                # 컨테이너 제거
                sh 'docker container ls -a -f name=frontend -q \
        | xargs -r docker container rm'
				sh 'docker container ls -a -f name=backend -q \
		| xargs -r docker container rm'

                sh 'docker run -d --name backend -p 8197:8197 backend:latest'
                sh 'docker run -d --name frontend -p 80:80 frontend:latest'
            }
        }
    }
}
```